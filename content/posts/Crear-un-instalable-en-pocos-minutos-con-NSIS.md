Title: Crear un instalable en pocos minutos con NSIS
Date: 2008-12-19 00:54:42
Category: Spanish
Tags: nsis, installer, win32
Author: frommelmak

[NSIS](http://nsis.sourceforge.net/) (*Nullsoft Scriptable Install System*) permite empaquetar aplicaciones en un fichero `.exe` autoinstalable. Aplicaciones como [OpenVPN](http://www.openvpn.se/download.html) (para Windows) o [VLC](http://www.videolan.org/) lo utilizan para distribuir sus versiones para plataformas Win32.

Pese a que la aplicación esta ampliamente [documentada](http://nsis.sourceforge.net/Docs/), he querido escribir este mini-articulo, en el que mediante un ejemplo explico los pasos a seguir para distribuir una aplicación. La idea es que dicho ejemplo sirva de base para no tener que perder mucho tiempo leyendo documentación y realizando mil y una pruebas antes de poder generar un instalable. Podeis utilizar el ejemplo como punto de partida para luego añadir lo que se os ocurra. Para ello os recomiendo dar un vistazo al [rincón de desarrolladores](http://nsis.sourceforge.net/Developer_Center) de la wiki del proyecto NSIS.

Para crear un instalable `.exe` con NSIS lo único que necesitamos es instalar la aplicación NSIS y crear un fichero de texto con extensión `.nsi`. Este fichero define -mediante un lenguaje de script propio- cómo ha de ser el instalable: apariencia, ficheros a instalar, directorio de instalación , selección de idioma, comprobaciones a realizar, modificar o leer el registro de Windows, descargar e instalar dependencias, acciones a realizar para la desinstalación. En definitiva, casi cualquier cosa que se nos pueda pasar por la cabeza.

Una vez tengamos nuestro fichero `.nsi`, crear el instalable es tan fácil como seleccionar nuestro fichero y desplegar el menu contextual. Tras seleccionarar la opción Compile NSIS Scirpt, aparecerá una consola con información acerca del progreso de generación del ejecutable, o en caso de error informacin relativa al fallo.

Pese a que NSIS permite personalizar el aspecto del instalador incrustando una imagen mediante las instrucciones `AddBrandingImage` y `SetBrandingImage`, es posible extender estas capacidades utilizando [NSIS Modern User Interface](http://nsis.sourceforge.net/Docs/Modern%20UI%202/Readme.html) o [Ultra Modern User Inteface](http://ultramodernui.sourceforge.net/).

El ejemplo que sigue a continuación utiliza Modern UI para crear un instalador resultón en un momento. Pare ser honestos, he de reconocer que pese a la fántastica documentación de NSIS, he perdio un buen rato intentando mejoar el look and feel del instalable mediante Modern UI debido a un problema que no he encontrado descrito en ningun sitio. El problema es que las imagenes de la cabecera no se muestran si no se incluye la instrucción `!insertmacro MUI_LANGUAGE lang`, que a priori no tiene nada que ver.

El ejemplo esta cargado de comentarios por lo que será fácil adaptarlo a vuestras necesidades. Para entenderlo simplemente hay que saber que el fichero `.nsi` esta ubicado en el mismo directorio que contiene los ficheros que conforman la aplicación que queremos instalar, así como las imagenes que utilizaremos para el wizard de instalación.

    :::console
     --FooApp
         |    `--lib
         |     |--file1.dll
         |     `--fileN.dll
         |-- header.bmp
         |-- image1.bmp
         |-- foo_app.ico
         |-- start_foo.exe 
         |-- foo_app.nsi
         `-- README.txt

El fichero `foo_app.nsi` encargado de crear el instalable para esta aplicacin podria ser este:

    :::nsis
    ;----------------------------------------------------------------------------
    ; General configuration
    
    ; The name and version of the installer
    
     !define VERSION 1.0
     Name Foo App ${VERSION}
     OutFile Foo App Installer - ${VERSION}.exe
     InstallDir $PROGRAMFILES\Foo App
    
     ;;; Request application privileges for Windows Vista (can be user or admin)
     RequestExecutionLevel admin
    ;----------------------------------------------------------------------------
    
    
    ;--------------------------------
    ;Use Modern User Interface
     !include MUI2.nsh
    ;--------------------------------
    
    
    ;--------------------------------
    ; Interface Settings

     BrandingText Foo App Installer (Powered by NSIS)
     !define MUI_HEADERIMAGE
     !define MUI_HEADERIMAGE_BITMAP header.bmp ; size 150x57
     !define MUI_HEADERIMAGE_UNBITMAP header.bmp ; size 150x57
     !define MUI_PAGE_HEADER_TEXT Installing Foo App
     !define MUI_PAGE_HEADER_SUBTEXT Copying files...
     !define MUI_ABORTWARNING
     !define MUI_ICON foo_app.ico
     !define MUI_UNICON foo_app.ico
    
    ; Pages
    
     !define MUI_WELCOMEFINISHPAGE_BITMAP image1.bmp ; size 164x314
     !define MUI_WELCOMEPAGE_TITLE_3LINES
     !define MUI_WELCOMEPAGE_TITLE Welcome to the Foo App ${VERSION} $\n Setup Wizard
     !define MUI_WELCOMEPAGE_TEXT This wizard will guide you through the installation of \
     Foo App ${VERSION} $\n$\nClick Install to continue
    
     !define MUI_INSTFILESPAGE_FINISHHEADER_TEXT Foo App Setup Complete
     !define MUI_INSTFILESPAGE_COLORS f1f1f1 000000
     !define MUI_FINISHPAGE_NOAUTOCLOSE
    
     !define MUI_FINISHPAGE_TITLE Setup Complete
     !define MUI_FINISHPAGE_TEXT Thank you for using Foo App
     !define MUI_FINISHPAGE_RUN foo.exe
     !define MUI_FINISHPAGE_RUN_TEXT Start Foo App
     
     !define MUI_UNCONFIRMPAGE_TEXT_TOP Remove Foo App from this computer
     !define MUI_UNCONFIRMPAGE_TEXT_LOCATION Installation Directory:
    
     !insertmacro MUI_PAGE_WELCOME
     !insertmacro MUI_PAGE_INSTFILES
     !insertmacro MUI_PAGE_FINISH
    
     !insertmacro MUI_UNPAGE_CONFIRM
     !insertmacro MUI_UNPAGE_INSTFILES
    
     ShowInstDetails show
     ShowUninstDetails show
    ;---------------------------------------------
    
    ;---------------------------------------------
    ; I don't know why but required to show images
    
     !insertmacro MUI_LANGUAGE English
    ;---------------------------------------------
    
    ;--------------------------------
    ; The stuff to install
    Section Install
     ;;; Foo App will be installed for all users
     SetShellVarContext all
     ;;; Set output path to the installation directory.
     SetOutPath $INSTDIR
     ;;; Put *.exe file there
     File start_foo.exe
     File README.txt
     File foo_app.ico
     File image1.bmp
     File header.bmp
     SetOutPath $INSTDIR\lib
     File lib\*.dll
     WriteUninstaller $INSTDIR\uninstaller.exe
     SetOutPath $INSTDIR
     ;;; Create desktop shortcut
     CreateShortCut $DESKTOP\Foo App.lnk $INSTDIR\start_foo.exe  $INSTDIR\foo_app.ico
     ;;; Create start-menu items
     CreateDirectory $STARTMENU\Foo App
     CreateShortCut $STARTMENU\Foo App\Foo App.lnk $INSTDIR\start_foo.exe  $INSTDIR\foo_app.ico
     CreateShortCut $STARTMENU\Foo App\Foo App Uninstaller.lnk $INSTDIR\uninstaller.exe
     ;;; Add uninstall information to Add/Remove Programs (Control Panel)
     WriteRegStr HKLM Software\Microsoft\Windows\CurrentVersion\Uninstall\FooApp \
     DisplayName Foo App Bla Bla
     WriteRegStr HKLM Software\Microsoft\Windows\CurrentVersion\Uninstall\FooApp \
     UninstallString $INSTDIR\uninstaller.exe
     WriteRegStr HKLM Software\Microsoft\Windows\CurrentVersion\Uninstall\FooApp \
     DisplayIcon $INSTDIR\foo_app.ico
     WriteRegStr HKLM Software\Microsoft\Windows\CurrentVersion\Uninstall\FooApp \
     Publisher Your Organization
    SectionEnd
    ;--------------------------------
    
    ;--------------------------------
    ; The stuff to Uninstall
    Section Uninstall
     ;;; Foo App will be removed for all users
     SetShellVarContext all
     SetOutPath $INSTDIR
     RMDir /r $INSTDIR
     RMDir /r $STARTMENU\Foo App
     Delete $DESKTOP\Foo App.lnk
     ;;; Remove Foo App info from the windows registry
     DeleteRegKey HKLM Software\Microsoft\Windows\CurrentVersion\Uninstall\FooApp
    SectionEnd
    ;--------------------------------
