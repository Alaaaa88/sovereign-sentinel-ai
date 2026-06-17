cmake_minimum_required(VERSION 3.20)
project(SovereignSentinelCore LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# البحث عن مكتبة nlohmann_json الحقيقية المثبتة على النظام
find_package(nlohmann_json 3.11.3 REQUIRED)

include_directories(include)

add_executable(sentinel_core src/main.cpp src/parser.cpp)

# ربط المكتبة بالملف التنفيذي
target_link_libraries(sentinel_core PRIVATE nlohmann_json::nlohmann_json)
