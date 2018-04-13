package cn.edu.zjut.maldetect;

import brut.androlib.AndrolibException;
import brut.directory.DirectoryException;

import java.io.IOException;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) throws AndrolibException, IOException, DirectoryException {
        final String path = "C:\\Users\\Fururur\\Downloads\\Compressed\\Android\\4\\";
        final String outPath = "unpacked\\1\\";
        DecodeApk.decodeBatch(path, outPath);
        DecodeApk.deleteUselessFiles(outPath);
        System.out.println("done...");
    }
}
