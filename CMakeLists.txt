cmake_minimum_required(VERSION 3.10)
project(guitar_project)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(guitar_synth src/main.cpp src/GuitarString.cpp)

target_include_directories(guitar_synth PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)