package cn.edu.zjut.maldetect;

import brut.androlib.AndrolibException;
import brut.androlib.ApkDecoder;
import brut.directory.DirectoryException;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * unpack apk
 *
 * @author Fururur
 * @create 2018-03-13-10:02
 */
public class DecodeApk {
    /**
     * unpack apk batch
     *
     * @param path training set path
     */
    public static void decodeBatch(String path, String outPath) {
        File trainingSet = new File(path);
        List<File> apks = new ArrayList<>();
        if (trainingSet.exists()) {
            File[] files = trainingSet.listFiles();
            apks = Arrays.asList(files != null ? files : new File[0]);
        }
        apks.forEach(apk -> {
            ApkDecoder decoder = new ApkDecoder();
            try {
                decoder.setOutDir(new File(outPath + apk.getName()));
                decoder.setApkFile(apk);
                decoder.decode();
            } catch (AndrolibException | IOException | DirectoryException e) {
                e.printStackTrace();
            }
        });
    }

    /**
     * delete useless file from unpacked apk folders except smali folders and AndroidManifest.xml
     *
     * @param path training set path
     */
    public static void deleteUselessFiles(String path) {
        final String manifest = "AndroidManifest";
        final String smaliFolders = "smali";
        File rootFolder = new File(path);
        List<File> apks = new ArrayList<>();
        if (rootFolder.exists()) {
            apks = Arrays.asList(rootFolder.listFiles());
        }
        apks.forEach(apk -> {
            File[] files = apk.listFiles();
            System.out.println(apk.getName());
            for (File f : files) {
                if (f.getName().contains(manifest) || f.getName().contains(smaliFolders))
                    continue;
                deleteDir(f);
            }
        });
    }


    /**
     * delete file and folder
     *
     * @param dir
     * @return
     */
    private static boolean deleteDir(File dir) {
        if (dir.isDirectory()) {
            String[] children = dir.list();
            for (String aChildren : children) {
                boolean success = deleteDir(new File(dir, aChildren));
                if (!success) {
                    return false;
                }
            }
        }
        return dir.delete();
    }
}
