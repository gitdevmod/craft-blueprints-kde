import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
#    def registerOptions(self):
#        self.options.dynamic.setDefault("buildType", "Debug")

    def setTargets(self):
        for ver in ['3.3.1']:
            self.targets[ver] = 'https://tellico-project.org/files/tellico-' + ver + '.tar.xz'
            self.targetInstSrc[ver] = 'tellico-' + ver
            self.targetDigestUrls[ver] = ([f"https://tellico-project.org/files/tellico-{ver}.tar.xz.md5"], CraftHash.HashAlgorithm.MD5)
        self.description = "Collection management software, free and simple"
        self.displayName = "Tellico"
        self.webpage = "https://tellico-project.org/"
        self.defaultTarget = '3.3.1'

    def setDependencies(self):
       self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
       self.buildDependencies["libs/gettext"] = None
       self.buildDependencies["kde/frameworks/tier1/karchive"] = None
       self.buildDependencies["kde/frameworks/tier1/kcodecs"] = None
       self.buildDependencies["kde/frameworks/tier1/kconfig"] = None
       self.buildDependencies["kde/frameworks/tier1/kcoreaddons"] = None
       self.buildDependencies["kde/frameworks/tier1/kguiaddons"] = None
       self.buildDependencies["kde/frameworks/tier1/ki18n"] = None
       self.buildDependencies["kde/frameworks/tier1/kitemmodels"] = None
       self.buildDependencies["kde/frameworks/tier1/solid"] = None
       self.buildDependencies["kde/frameworks/tier1/kwidgetsaddons"] = None
       self.buildDependencies["kde/frameworks/tier1/kwindowsystem"] = None
       self.buildDependencies["kde/frameworks/tier3/kconfigwidgets"] = None
       self.buildDependencies["kde/frameworks/tier2/kcrash"] = None
       self.buildDependencies["kde/frameworks/tier2/kdoctools"] = None
       self.buildDependencies["kde/frameworks/tier2/kfilemetadata"] = None
       self.buildDependencies["kde/frameworks/tier2/kjobwidgets"] = None
       self.buildDependencies["kde/frameworks/tier3/khtml"] = None
       self.buildDependencies["kde/frameworks/tier3/kiconthemes"] = None
       self.buildDependencies["kde/frameworks/tier3/kio"] = None
       self.buildDependencies["kde/frameworks/tier3/knewstuff"] = None
       self.buildDependencies["kde/frameworks/tier3/kwallet"] = None
       self.buildDependencies["kde/frameworks/tier3/kxmlgui"] = None
       self.runtimeDependencies["virtual/base"] = None
       self.runtimeDependencies["kde/plasma/drkonqi"] = None
       self.runtimeDependencies["libs/qt5/qtbase"] = None
