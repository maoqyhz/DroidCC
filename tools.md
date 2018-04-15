> collected from [impillar / AndroidReferences](https://github.com/impillar/AndroidReferences)

## Forensics Tools

- [Android Forensics](https://github.com/viaforensics/android-forensics) – Open Source Android Forensics App and Framework
- [Android Data Extractor Lite](https://github.com/mspreitz/ADEL)
- [BitPim](http://www.bitpim.org/) – BitPim is a program that allows you to view and manipulate data on many CDMA phones from LG, Samsung, Sanyo and other manufacturers.
- [LiME](https://github.com/504ensicsLabs/LiME) – LiME (formerly DMD) is a Loadable Kernel Module (LKM), which allows the acquisition of volatile memory from Linux and Linux-based devices, such as those powered by Android.
- [Open Source Android Forensics](http://www.osaf-community.org/)
- [P2P-ADB](https://github.com/kosborn/p2p-adb/) – Phone to Phone Android Debug Bridge – A project for “debugging” phones from other phones.
- [pySimReader](https://www.isecpartners.com/tools/mobile-security/pysimreader.aspx) – It allows users to write out arbitrary raw SMS PDUs to a SIM card.

## Development Tools

- [Android SDK](https://developer.android.com/sdk/index.html) – The Android software development kit (SDK) includes a comprehensive set of development tools. These include a debugger, libraries, a handset emulator based on QEMU, documentation, sample code, and tutorials.
- [Android NDK](https://developer.android.com/tools/sdk/ndk/index.html) – The NDK is a toolset that allows you to implement parts of your app using native-code languages such as C and C--.
- [ADT Bundle](https://developer.android.com/sdk/index.html) – The Android Developer Tools(ADT) bundle is a single download that contains everything for developers to start creating Android Application
  * Android Studio IDE or Eclipse IDE
  * Android SDK tools
  * Android 5.0 (Lollipop) Platform
  * Android 5.0 emulator system image with Google APIs
- [Native Android Runtime Emulation](https://bitbucket.org/jigsaw_echo/armexec) – A native Android emulator featuring the following functions:
  * Full stack support for ELF built by Android NDK.
  * Seeminglessly native gdb support.
  * Link and load shared library.
  * Open to extension of different architecture and C runtime.
- [Root Tools](https://github.com/Stericson/RootTools) – RootTools provides rooted developers a standardized set of tools for use in the development of rooted applications.

## Static Analysis Tools

- [Androwarn](https://github.com/maaaaz/androwarn/) - Yet another static code analyzer for malicious Android applications
- [ApkAnalyser](https://github.com/sonyxperiadev/ApkAnalyser) – ApkAnalyser is a static, virtual analysis tool for examining and validating the development work of your Android app.
- [APKInspector](https://github.com/honeynet/apkinspector/) – APKinspector is a powerful GUI tool for analysts to analyze the Android applications.
- [DroidSafe](http://mit-pac.github.io/droidsafe-src/) – The DroidSafe project develops novel program analysis techniques to diagnose and remove malicious code from Android mobile applications. The clone is located at DroidSafe-GitHub.
- [Crashlytics](https://try.crashlytics.com/) - Crashlytics is a powerful, yet light-weight crash reporting solution
- [Error-Prone](https://github.com/google/error-prone) – Catch common Java mistakes as compile-time errors
- [FindBugs](http://findbugs.sourceforge.net/) - [FindSecurityBugs](http://h3xstream.github.io/find-sec-bugs/) – FindSecurityBugs is a extension for FindBugs which include security rules for Java applications. It will find cryptography problems as well as Android specific problems.
- [ApkCombiner](https://github.com/lilicoding/ApkCombiner) - Combining multiple Android apps to one for supporting inter-app analysis
- [IC3](https://github.com/siis/ic3) - Inter-Component Communication Analysis with COAL
- [FlowDroid](http://sseblog.ec-spride.de/tools/flowdroid/) – FlowDroid is a context-, flow-, field-, object-sensitive and lifecycle-aware static taint analysis tool for Android applications.
- [IccTA](https://github.com/lilicoding/soot-infoflow-android-iccta) - An Inter-Component Communication based Taint Analysis tool based on FlowDroid and Epicc/IC3 to perform inter-component privacy leaks in Android apps
- [Lint](http://developer.android.com/tools/help/lint.html) – The Android lint tool is a static code analysis tool that checks your Android project source files for potential bugs and optimization improvements for correctness, security, performance, usability, accessibility, and internationalization.
- [PMD](http://pmd.sourceforge.net/) – PMD is a source code analyzer. It finds common programming flaws like unused variables, empty catch blocks, unnecessary object creation, and so forth. It supports Java, Javascript, XML, XSL.
- [Smali CFGs](https://github.com/EugenioDelfa/Smali-CFGs) – Smali Control Flow Graph’s
- [Smali and Baksmali](https://code.google.com/p/smali/) – smali/baksmali is an assembler/disassembler for the dex format used by dalvik, Android’s Java VM implementation.
- [Thresher](http://pl.cs.colorado.edu/projects/thresher/) – Thresher is a static analysis tool that specializes in checking heap reachability properties. Its secret sauce is using a coarse up-front points-to analysis to focus a precise symbolic analysis on the alarms reported by the points-to analysis.
- [SuSi](https://github.com/secure-software-engineering/SuSi) - automatically discover and categorize sources and sinks in the Android framework

## Dynamic Analysis Tools

- [Android Hooker](https://github.com/AndroidHooker/hooker) – This project provides various tools and applications that can be use to automaticaly intercept and modify any API calls made by a targeted application.
- [Droidbox](https://code.google.com/p/droidbox/) – DroidBox is developed to offer dynamic analysis of Android applications
- [Drozer](https://www.mwrinfosecurity.com/products/drozer/) – Drozer allows you to search for security vulnerabilities in apps and devices by assuming the role of an app and interacting with the Dalvik VM, other apps’ IPC endpoints and the underlying OS.
- [TaintDroid](http://appanalysis.org/) – Tracking how apps use sensitive information required integrating our software into the Android platform at a low level.
- [Xposed Framework](http://forum.xda-developers.com/xposed/xposed-installer-versions-changelog-t2714053)
- [Inspeckage](http://ac-pm.github.io/Inspeckage/) - Inspeckage is a tool developed to offer dynamic analysis of Android applications. By applying hooks to functions of the Android API, Inspeckage will help you understand what an Android application is doing at runtime.


## Reverse Engineering Tools

- [Androguard](https://github.com/androguard/androguard) – Reverse engineering, Malware and goodware analysis of Android applications … and more (ninja !)
- [dockerfile-androguard] (https://github.com/dweinstein/dockerfile-androguard) - Docker file for building androguard dependencies w/ an optional interactive shell environment
- [Android loadble Kernel Modules](https://github.com/strazzere/android-lkms) – It is mostly used for reversing and debugging on controlled systems/emulators.
- [AndBug](https://github.com/swdunlop/AndBug) – Android Debugging Library
- [ApkTool](https://code.google.com/p/android-apktool/) – A tool for reverse engineering Android Apk Files
- [APK Studio](https://apkstudio.codeplex.com/) – APK Studio is an IDE for decompiling/editing & then recompiling of android application binaries.
- [Bytecode-Viewer](https://github.com/Konloch/bytecode-viewer) – A Java 8 Jar & Android APK Reverse Engineering Suite (Decompiler, Editor, Debugger & More)
- [CodeInspect](http://sseblog.ec-spride.de/2014/12/codeinspect/) – A Jimple-based Reverse-Engineering framework for Android and Java applications.
- [dedex](https://github.com/mariokmk/dedex) – A command line tool for disassembling Android DEX files.
- [enjarify](https://github.com/google/enjarify) - A tool for translating Dalvik bytecode to equivalent Java bytecode :star:
- [Dex2Jar](https://code.google.com/p/dex2jar/) – Tools to work with android .dex and java .class files
- [dexdisassembler](https://github.com/mariokmk/dexdisassembler) – A GTK tool for disassembling Android DEX files.
- [Fern Flower](https://github.com/fesh0r/fernflower) – FernFlower Java decompiler
- [Fino](https://github.com/sysdream/fino) – Android small footprint inspection tool
- [Introspy-Android](https://github.com/iSECPartners/Introspy-Android) – Blackbox tool to help understand what an Android application is doing at runtime and assist in the identification of potential security issues.
- [JD-Gui](http://jd.benow.ca/) – Yet another fast Java Decompiler
- [JEB](https://www.pnfsoftware.com/index) – The Interactive Android Decompiler
- [smali](https://code.google.com/p/smali/) – An assembler/disassembler for Android’s dex format

##Hooking Tools

- [ADBI Framework](https://github.com/crmulliner/ddi) – Simple and easy to use toolkit for dynamic instrumentation of Dalvik code.
- [Cydia Substrate](http://www.cydiasubstrate.com/) – Cydia Substrate for Android enables developers to make changes to existing software with Substrate extensions that are injected in to the target process’s memory.
- [Xposed Framework](http://forum.xda-developers.com/xposed/xposed-installer-versions-changelog-t2714053) – Xposed framework enables you to modify the system or application aspect and behaviour at runtime, without modifying any Android application package(APK) or re-flashing.
- [Dexposed](https://github.com/alibaba/dexposed) - Dexposed is a powerful yet non-invasive runtime AOP (Aspect-oriented Programming) framework for Android app development, based on the work of open-source Xposed framework project.
- [Frida](http://www.frida.re/) – Inject JavaScript to explore native apps on Android
- [ELLA](https://github.com/saswatanand/ella) - Ella is a tool to instrument Android APK's for various purposes. Out of the box, it instruments apps to record which methods gets executed. It can also record time-stamped trace of executed methods, values of arguments passed at call-sites, values of formal parameters of methods, etc.

## Obfuscators & Deobfuscators Tools

- [APK Obfuscator](https://github.com/strazzere/APKfuscator) – A generic DEX file obfuscator and munger.
- [Bytecode-Viewer](https://github.com/Konloch/bytecode-viewer) – A Java 8 Jar & Android APK Reverse Engineering Suite (Decompiler, Editor, Debugger & More)
- [Class Name Deobfuscator](https://github.com/HamiltonianCycle/ClassNameDeobfuscator) – Simple script to parse through the .smali files produced by apktool and extract the .source annotation lines.
- [Dalvik Obfuscator](https://github.com/thuxnder/dalvik-obfuscator) – A set of tools/scripts to obfuscate and manipulate dex files
- [Simplify](https://github.com/CalebFenton/simplify) – Generic Android Deobfuscator

## Online Analyzers

- [Android Observatory](https://androidobservatory.org/) – The Android Observatory is a web interface to a large repository of Android applications. It allows users to search or browse through thousands of Android apps and retrieve metadata for those apps.
- [Android APK Decompiler](http://www.decompileandroid.com/) – Decompiling APK files made easy. Online decompiler.
- [AndroidTotal](http://andrototal.org/) – AndroTotal is a free service to scan suspicious APKs against multiple mobile antivirus apps.
- [Anubis](http://anubis.iseclab.org/) – Malware Analysis for Unknown Binaries.
- [Akana](http://www.mobiseclab.org/akana/Intro.html) – Akana is an online Android app Interactive Analysis Enviroment (IAE), which is combined with some plugins for checking the malicious app.
- [App360Scan](http://www.app360scan.com/) – Tells about permissons used by an Application and what harm it can cause to users.
- [Baidu](http://seclab.safe.baidu.com/) – It provides an online security analysis of Android apps.
- [CopperDroid](http://copperdroid.isg.rhul.ac.uk/copperdroid/) – It automatically perform out-of-the-box dynamic behavioral analysis of Android malware.
- [Dexter](https://dexter.bluebox.com/) – Dexter is an interactive Android software analysis environment with collaboration features.
- [Eacus](http://www.mobiseclab.org/eacus.jsp) – A lite Android app analysis framework
- [Mobile Sandbox](http://mobilesandbox.org/) – The Mobile-Sandbox provides static and dynamic malware analysis combined with machine learning techniques for Android applications.
- [Sandroid](http://sanddroid.xjtu.edu.cn/#overview) – An automatic Android application analysis system
- [Virus Total](https://www.virustotal.com/) – VirusTotal is a free service that analyzes suspicious files and URLs and facilitates the quick detection of viruses, worms, trojans, and all kinds of malware.

## Android Testing Distributions

- [Appie](https://manifestsecurity.com/appie) – A portable software package for Android Pentesting and an awesome alternative to existing Virtual machines.It is a one stop answer for all the tools needed in Android Application Security Assessment, Android Forensics, Android Malware Analysis.
- [Android Tamer](https://androidtamer.com/) – Android Tamer is a Virtual / Live Platform for Android Security professionals.
- [AppUse](https://appsec-labs.com/AppUse/) – AppUse is a VM (Virtual Machine) developed by AppSec Labs.
- [Mobisec](http://sourceforge.net/projects/mobisec/) – Mobile security testing live environment
- [Now Secure App Testing Suite:Community Edition](https://www.nowsecure.com/apptesting/community/#viaprotect)
- [Santoku Linux](https://santoku-linux.com/) – Santoku Linux is a virtual machine developed by NowSecure Mobile.
- [Shadow OS](http://h30499.www3.hp.com/t5/Fortify-Application-Security/Announcing-ShadowOS/ba-p/6725771#.VUzhUJOupKg) – ShadowOS is a free tool designed by Fortify on Demand to help Security and QA teams test Android applications for security vulnerabilities. It is a custom OS based off of KitKat that intercepts specific areas of the device’s operation and makes testing apps for security vulnerabilites easier.
- [Vezir Project](https://github.com/oguzhantopgul/Vezir-Project) – Yet Another Linux Virtual Machine for Mobile Application Pentesting and Mobile Malware Analysis.
- [AndroidJUnitRunner](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner.html) - An Instrumentation that runs JUnit3 and JUnit4 tests against an Android package (application).
- [Espresso](https://google.github.io/android-testing-support-library/docs/espresso/) – 

## Android Vulnerable Apps

- [Android Challenges of Various Conferences/Events](https://drive.google.com/folderview?id=0B7rtSe_PH_fTWDQ0RC1DeWVoVUE&usp=sharing)
- [Owasp Goatdroid Project](https://github.com/jackMannino/OWASP-GoatDroid-Project)
- [ExploitMe labs by SecurityCompass](http://securitycompass.github.io/AndroidLabs/setup.html)
- [InsecureBank V2](https://github.com/dineshshetty/Android-InsecureBankv2)
- [Sieve](https://labs.mwrinfosecurity.com/system/assets/380/original/sieve.apk)– Sieve is a password manager app, riddled with security vulnerabilities.

## Android Security Apps

- [Android IMSI-Catcher-Detector](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector) – It is an app to detect IMSI-Catchers. IMSI-Catchers are false mobile towers (base stations) acting between the target mobile phone(s) and the real towers of service providers. As such they are considered a Man-In-The-Middle (MITM) attack. In the USA the IMSI-Catcher technology is known under the name “StingRay”.
- [Am I Vulnerable](http://delhi.securitycompass.com/) – AIV is an Android security app that notifies the user of publicly known vulnerabilities found in the installed version of apps on the device.

## Application Security Framework

- [AppRay](http://www.app-ray.com/) – App-Ray takes a look inside your apps and helps you understand what they really do. In fully automated tests, App-Ray analyzes apps and highlights vulnerabilities, data leaks, and privacy breaches.
- [YSO-Mobile Security Framework](https://github.com/ajinabraham/YSO-Mobile-Security-Framework) – Mobile Security Framework is an intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static and dynamic analysis.

## Android Malwares Related

- [Contagio Mini Dump](http://contagiominidump.blogspot.com/) – Contagio mobile mini-dump offers an upload dropbox for you to share your mobile malware samples.
- [Android Malwares Databases](https://code.google.com/p/androguard/wiki/DatabaseAndroidMalwares) – No Longer Maintained.
- [Android Malware Evaluating Tools](https://github.com/faber03/AndroidMalwareEvaluatingTools) – Evaluation tools for Android Malwares
- [Maldrolyzer](https://github.com/maldroid/maldrolyzer) – Simple framework to extract “actionable” data from Android malware (C&Cs, phone numbers etc.)

## Tutorials

- [Android Application Security Series](https://manifestsecurity.com/android-application-security/) – A simple and elaborative series on Android Application Security. Beneficial for Android Security Professionals and Developers.
- [Android Forensics Course](http://opensecuritytraining.info/AndroidForensics.html)
- [Introduction to ARM](http://opensecuritytraining.info/IntroARM.html)
- [Android Security Articles By Infosec Institute](http://resources.infosecinstitute.com/author/srinivas/)
- [Learning Android Bytecode](https://mariokmk.github.io/programming/2015/03/06/learning-android-bytecode.html)

## Android Vulnerability List

- [Android Vulnerability/Exploit List](https://docs.google.com/spreadsheet/pub?key=0Am5hHW4ATym7dGhFU1A4X2lqbUJtRm1QSWNRc3E0UlE&single=true&gid=0&output=html)
- [Android CVE Details](http://www.cvedetails.com/vulnerability-list/vendor_id-1224/product_id-19997/Google-Android.html)

## Android Security Libraries

- [Android Password Store](https://github.com/zeapo/Android-Password-Store)
- [Android Pinning](https://github.com/moxie0/AndroidPinning) – A standalone library project for certificate pinning on Android.
- [Conceal By Facebook](https://github.com/facebook/conceal) – Conceal provides easy Android APIs for performing fast encryption and authentication of data.
- [Dexguard](http://www.saikoa.com/dexguard) – DexGuard is our specialized optimizer and obfuscator for Android. Create apps that are faster, more compact, and more difficult to crack.
- [Encryption](https://github.com/simbiose/Encryption) – Encryption is a simple way to create encrypted strings to Android project.
- [CWAC-Security](https://github.com/commonsguy/cwac-security) – Helping You Help Your Users Defend Their Data
- [IOCipher](https://github.com/guardianproject/IOCipher) – IOCipher is a virtual encrypted disk for apps without requiring the device to be rooted.
- [Java AES Crypto](https://github.com/tozny/java-aes-crypto) – A simple Android class for encrypting & decrypting strings, aiming to avoid the classic mistakes that most such classes suffer from.
- [NetCipher](https://github.com/guardianproject/NetCipher) – This is an Android Library Project that provides multiple means to improve network security in mobile applications.
- [OpenPGP API](https://github.com/open-keychain/openpgp-api-lib) – The OpenPGP API provides methods to execute OpenPGP operations, such as sign, encrypt, decrypt, verify, and more without user interaction from background threads.
- [OWASP Java HTML Sanitizer](https://code.google.com/p/owasp-java-html-sanitizer/)
- [Proguard](http://proguard.sourceforge.net/) – ProGuard is a free Java class file shrinker, optimizer, obfuscator, and preverifier. It detects and removes unused classes, fields, methods, and attributes.
- [Spongy Castle](https://github.com/rtyley/spongycastle) – a repackage of Bouncy Castle for Android
- [SQL Cipher](https://www.zetetic.net/sqlcipher/sqlcipher-for-android/) – SQLCipher is an open source extension to SQLite that provides transparent 256-bit AES encryption of database files.
- [Secure Preferences](https://github.com/scottyab/secure-preferences) – Android Shared preference wrapper than encrypts the keys and values of Shared Preferences.
- [Trusted Intents](https://github.com/guardianproject/TrustedIntents) – Library for flexible trusted interactions between Android apps

## Best Practices

- [Android Security Overview](http://source.android.com/devices/tech/security/)
- [Android Security Tips for Developers](http://developer.android.com/training/articles/security-tips.html)
- [Projects/OWASP Mobile Security Project – Top Ten Mobile Controls](https://www.owasp.org/index.php/Projects/OWASP_Mobile_Security_Project_-_Top_Ten_Mobile_Controls)
- [PCI Mobile Payment Acceptance Security Guidelines for Developers](https://www.pcisecuritystandards.org/documents/Mobile%20Payment%20Security%20Guidelines%20v1%200.pdf)
- [Secure Coding in Android](https://www.securecoding.cert.org/confluence/pages/viewpage.action?pageId=111509535)

## Android App Crawler
- [APK Downloader](http://apps.evozi.com/apk-downloader/): A web service to take package name as input, and generate a link to download apps in Google Play.
- [Gplaycli](https://github.com/matlink/gplaycli): A framework to download Android apps from Google Play via command line
