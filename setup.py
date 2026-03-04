#!/usr/bin/env python3
import os, base64, gzip

def mkdir(p): os.makedirs(p, exist_ok=True)
def write(path, content):
    mkdir(os.path.dirname(path) or '.')
        open(path,'w',encoding='utf-8').write(content)
            print("  OK " + path)
            def write_bytes(path, data):
                mkdir(os.path.dirname(path) or '.')
                    open(path,'wb').write(data)
                        print("  OK " + path)

                        print("Creating Android project...")

                        write("settings.gradle",
                        "pluginManagement {\n    repositories { google(); mavenCentral(); gradlePluginPortal() }\n}\n"
                        "dependencyResolutionManagement {\n    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)\n"
                        "    repositories { google(); mavenCentral() }\n}\n"
                        "rootProject.name = \"YawmiyatFallah\"\ninclude ':app'\n")

                        write("build.gradle","plugins { id 'com.android.application' version '8.2.2' apply false }\n")
                        write("gradle.properties","org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8\nandroid.useAndroidX=true\nandroid.enableJetifier=true\n")
                        write("gradle/wrapper/gradle-wrapper.properties",
                        "distributionBase=GRADLE_USER_HOME\ndistributionPath=wrapper/dists\n"
                        "distributionUrl=https\://services.gradle.org/distributions/gradle-8.4-bin.zip\n"
                        "zipStoreBase=GRADLE_USER_HOME\nzipStorePath=wrapper/dists\n")
                        write("gradlew","#!/bin/sh\nAPP_HOME=$(dirname \"$0\")\nexec java -classpath \"$APP_HOME/gradle/wrapper/gradle-wrapper.jar\" org.gradle.wrapper.GradleWrapperMain \"$@\"\n")
                        os.chmod("gradlew",0o755)
                        write("app/build.gradle",
                        "plugins { id 'com.android.application' }\n"
                        "android {\n    namespace 'com.yawmiyat.fallah'\n    compileSdk 34\n"
                        "    defaultConfig {\n        applicationId \"com.yawmiyat.fallah\"\n"
                        "        minSdk 21; targetSdk 34\n        versionCode 4; versionName \"1.0.3\"\n    }\n"
                        "    buildTypes { release { minifyEnabled false } }\n"
                        "    compileOptions {\n        sourceCompatibility JavaVersion.VERSION_1_8\n        targetCompatibility JavaVersion.VERSION_1_8\n    }\n}\n"
                        "dependencies {\n    implementation 'androidx.appcompat:appcompat:1.6.1'\n    implementation 'androidx.core:core:1.12.0'\n}\n")
                        write("app/proguard-rules.pro","-keep class com.yawmiyat.fallah.** { *; }\n")
                        write("app/src/main/AndroidManifest.xml",
                        "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<manifest xmlns:android=\"http://schemas.android.com/apk/res/android\">\n"
                        "    <uses-permission android:name=\"android.permission.INTERNET\"/>\n"
                        "    <application android:allowBackup=\"true\" android:icon=\"@mipmap/ic_launcher\"\n"
                        "        android:roundIcon=\"@mipmap/ic_launcher_round\" android:label=\"@string/app_name\"\n"
                        "        android:theme=\"@style/Theme.YawmiyatFallah\" android:hardwareAccelerated=\"true\" android:supportsRtl=\"true\">\n"
                        "        <activity android:name=\".MainActivity\" android:exported=\"true\"\n"
                        "            android:screenOrientation=\"portrait\" android:windowSoftInputMode=\"adjustResize\">\n"
                        "            <intent-filter>\n                <action android:name=\"android.intent.action.MAIN\"/>\n"
                        "                <category android:name=\"android.intent.category.LAUNCHER\"/>\n"
                        "            </intent-filter>\n        </activity>\n    </application>\n</manifest>\n")
                        write("app/src/main/java/com/yawmiyat/fallah/MainActivity.java",
                        "package com.yawmiyat.fallah;\n"
                        "import android.annotation.SuppressLint;\nimport android.graphics.Color;\nimport android.os.Bundle;\n"
                        "import android.view.View;\nimport android.webkit.*;\nimport androidx.appcompat.app.AppCompatActivity;\n"
                        "import androidx.core.view.WindowCompat;\nimport androidx.core.view.WindowInsetsControllerCompat;\n"
                        "public class MainActivity extends AppCompatActivity {\n    private WebView webView;\n"
                        "    @SuppressLint(\"SetJavaScriptEnabled\")\n    @Override\n    protected void onCreate(Bundle savedInstanceState) {\n"
                        "        super.onCreate(savedInstanceState);\n"
                        "        WindowCompat.setDecorFitsSystemWindows(getWindow(), false);\n"
                        "        getWindow().setStatusBarColor(Color.TRANSPARENT);\n"
                        "        getWindow().setNavigationBarColor(Color.TRANSPARENT);\n"
                        "        WindowInsetsControllerCompat c = WindowCompat.getInsetsController(getWindow(), getWindow().getDecorView());\n"
                        "        c.setAppearanceLightStatusBars(false);\n        c.setAppearanceLightNavigationBars(false);\n"
                        "        setContentView(R.layout.activity_main);\n        webView = findViewById(R.id.webview);\n"
                        "        WebSettings s = webView.getSettings();\n"
                        "        s.setJavaScriptEnabled(true); s.setDomStorageEnabled(true); s.setDatabaseEnabled(true);\n"
                        "        s.setAllowFileAccessFromFileURLs(true); s.setAllowUniversalAccessFromFileURLs(true);\n"
                        "        s.setUseWideViewPort(true); s.setLoadWithOverviewMode(true);\n"
                        "        s.setBuiltInZoomControls(false); s.setDisplayZoomControls(false);\n"
                        "        s.setDefaultTextEncodingName(\"UTF-8\"); s.setCacheMode(WebSettings.LOAD_NO_CACHE);\n"
                        "        CookieManager.getInstance().setAcceptCookie(true);\n"
                        "        CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);\n"
                        "        webView.setBackgroundColor(Color.parseColor(\"#080f08\"));\n"
                        "        webView.setLayerType(View.LAYER_TYPE_HARDWARE, null);\n"
                        "        webView.setOverScrollMode(View.OVER_SCROLL_NEVER);\n"
                        "        webView.setWebViewClient(new WebViewClient() {\n"
                        "            @Override public void onPageFinished(WebView view, String url) {\n"
                        "                super.onPageFinished(view, url);\n"
                        "                int sb = getStatusBarHeight(); int nb = getNavBarHeight();\n"
                        "                String js = \"var tb=document.querySelector('.topbar');\" +\n"
                        "                    \"if(tb){tb.style.paddingTop='\" + sb + \"px';tb.style.height=(48+\" + sb + \")+'px';}\" +\n"
                        "                    \"document.documentElement.style.setProperty('--status-bar-height','\" + sb + \"px');\";\n"
                        "                view.evaluateJavascript(js, null);\n"
                        "            }\n        });\n"
                        "        webView.setWebChromeClient(new WebChromeClient());\n"
                        "        webView.loadUrl(\"file:///android_asset/index.html\");\n    }\n"
                        "    private int getStatusBarHeight() {\n"
                        "        int id=getResources().getIdentifier(\"status_bar_height\",\"dimen\",\"android\");\n"
                        "        return id>0?getResources().getDimensionPixelSize(id):72;\n    }\n"
                        "    private int getNavBarHeight() {\n"
                        "        int id=getResources().getIdentifier(\"navigation_bar_height\",\"dimen\",\"android\");\n"
                        "        return id>0?getResources().getDimensionPixelSize(id):0;\n    }\n"
                        "    @Override public void onBackPressed() { if(webView!=null&&webView.canGoBack()) webView.goBack(); else super.onBackPressed(); }\n"
                        "    @Override protected void onDestroy() { if(webView!=null){webView.destroy();webView=null;} super.onDestroy(); }\n}\n")
                        write("app/src/main/res/layout/activity_main.xml",
                        "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
                        "<RelativeLayout xmlns:android=\"http://schemas.android.com/apk/res/android\"\n"
                        "    android:layout_width=\"match_parent\" android:layout_height=\"match_parent\" android:background=\"#080f08\">\n"
                        "    <WebView android:id=\"@+id/webview\"\n"
                        "        android:layout_width=\"match_parent\" android:layout_height=\"match_parent\"\n"
                        "        android:background=\"#080f08\" android:overScrollMode=\"never\" android:scrollbars=\"none\"/>\n"
                        "</RelativeLayout>\n")
                        write("app/src/main/res/values/strings.xml","<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources><string name=\"app_name\">يوميات الفلاح</string></resources>\n")
                        write("app/src/main/res/values/themes.xml",
                        "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
                        "    <style name=\"Theme.YawmiyatFallah\" parent=\"Theme.AppCompat.NoActionBar\">\n"
                        "        <item name=\"android:windowBackground\">#080f08</item>\n"
                        "        <item name=\"android:statusBarColor\">@android:color/transparent</item>\n"
                        "        <item name=\"android:navigationBarColor\">@android:color/transparent</item>\n"
                        "        <item name=\"android:windowTranslucentStatus\">false</item>\n"
                        "        <item name=\"android:windowDrawsSystemBarBackgrounds\">true</item>\n"
                        "    </style>\n</resources>\n")

                        # YAML ecrit ligne par ligne — pas de probleme d'indentation
                        yml_lines = [
                        "name: Build APK",
                        "on:",
                        "  push:",
                        "    branches: [ main ]",
                        "  workflow_dispatch:",
                        "jobs:",
                        "  build:",
                        "    runs-on: ubuntu-latest",
                        "    steps:",
                        "      - uses: actions/checkout@v4",
                        "      - uses: actions/setup-java@v4",
                        "        with:",
                        "          java-version: '17'",
                        "          distribution: 'temurin'",
                        "      - name: Gradle JAR",
                        "        run: |",
                        "          mkdir -p gradle/wrapper",
                        "          curl -sL https://raw.githubusercontent.com/gradle/gradle/v8.4.0/gradle/wrapper/gradle-wrapper.jar -o gradle/wrapper/gradle-wrapper.jar",
                        "      - name: Setup",
                        "        run: python3 setup.py",
                        "      - name: Build",
                        "        run: |",
                        "          chmod +x gradlew",
                        "          ./gradlew assembleDebug --no-daemon",
                        "      - uses: actions/upload-artifact@v4",
                        "        with:",
                        "          name: yawmiyat-fallah-apk",
                        "          path: app/build/outputs/apk/debug/app-debug.apk",
                        "          retention-days: 30",
                        ]
                        write(".github/workflows/build.yml", "\n".join(yml_lines) + "\n")

                        # Icons
                        try:
                            from PIL import Image, ImageDraw
                                def draw_icon(size):
                                        img=Image.new('RGB',(size,size),'#080f08'); d=ImageDraw.Draw(img); s,cx=size,size//2
                                                d.ellipse([int(s*.04)]*2+[s-int(s*.04)]*2,fill='#0d1c0a')
                                                        d.arc([int(s*.12),int(s*.58),int(s*.88),int(s*.86)],180,0,fill='#2c6014',width=max(2,s//28))
                                                                ty1=int(s*.40); d.line([cx,int(s*.72),cx,ty1],fill='#7a4a10',width=max(2,s//24))
                                                                        for x1,y1 in [(int(s*.22),int(s*.26)),(int(s*.30),int(s*.17)),(cx,int(s*.11)),(int(s*.70),int(s*.17)),(int(s*.78),int(s*.26))]:
                                                                                    d.line([cx,ty1,x1,y1],fill='#4a9020',width=max(1,s//32))
                                                                                            dr=max(2,s//22)
                                                                                                    for px,py,col in [(int(s*.38),int(s*.19),'#c8781a'),(cx,int(s*.13),'#d4881e'),(int(s*.62),int(s*.18),'#c8781a')]:
                                                                                                                d.ellipse([px-dr,py-dr,px+dr,py+dr],fill=col)
                                                                                                                        for wx in [int(s*.27),int(s*.73)]:
                                                                                                                                    d.line([wx,int(s*.78),wx,int(s*.44)],fill='#c8a020',width=max(1,s//36)); er=max(3,s//14)
                                                                                                                                                for cy2 in [int(s*.68),int(s*.59),int(s*.51)]: d.ellipse([wx-er,cy2-er//2,wx+er,cy2+er//2],fill='#c8a020')
                                                                                                                                                        sr=int(s*.10); d.ellipse([cx-sr,int(s*.33)-sr,cx+sr,int(s*.33)+sr],fill='#1a4a08')
                                                                                                                                                                d.ellipse([cx-int(s*.07),int(s*.33)-int(s*.07),cx+int(s*.07),int(s*.33)+int(s*.07)],fill='#82cc50')
                                                                                                                                                                        return img
                                                                                                                                                                            for folder,size in [('mipmap-mdpi',48),('mipmap-hdpi',72),('mipmap-xhdpi',96),('mipmap-xxhdpi',144),('mipmap-xxxhdpi',192)]:
                                                                                                                                                                                    base=f'app/src/main/res/{folder}'; mkdir(base); img=draw_icon(size)
                                                                                                                                                                                            img.save(f'{base}/ic_launcher.png'); img.save(f'{base}/ic_launcher_round.png')
                                                                                                                                                                                                    print("  OK " + base)
                                                                                                                                                                                                    except: print("  Pillow absent")

                                                                                                                                                                                                    html_b64 = "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