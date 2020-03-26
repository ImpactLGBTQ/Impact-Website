cmake_minimum_required(VERSION 3.1)
project(IMPACT_SETUP)

set(CMAKE_BINARY_DIR "cmake-build")
set(SRC main.cpp)

add_executable(${PROJECT_NAME} ${SRC})

target_link_libraries(${PROJECT_NAME} libapt)

