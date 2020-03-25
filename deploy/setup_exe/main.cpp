// Simple C++ program to setup the enviroment for the Impact Website. Why is it c++ you ask? becuase libapt thats why

#include <iostream>

// libapt
#include <apt-pkg/cachefile.h>
#include <apt-pkg/pkgcache.h>

int main(int argc, char** argv) {
    pkgInitConfig(*_config);
    pkgInitSystem(*_config, _system);
    
    pkgCacheFile cache_file;
    pkgCache* cache = cache_file.GetPkgCache();
    
    // Print all packages
    for (pkgCache::PkgIterator package = cache->PkgBegin(); !package.end(); package++) {
        std::cout << package.Name() << std::endl;
    }
}
