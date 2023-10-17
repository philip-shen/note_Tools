cmake_minimum_required(VERSION 3.27)
project(OpenCV_Cpp VERSION 1.0.0 LANGUAGES CXX)

# Copy resouce
#file(COPY ${CMAKE_SOURCE_DIR}/media/ DESTINATION ${PROJECT_BINARY_DIR}/media/)
#add_definitions(-DRESOURCE_DIR="${PROJECT_BINARY_DIR}/media/")

# Create Main project
set(SOURCES
    68_hough_circle_transform.cpp
)

set(HEADERS
    # main.h
)

add_executable(OpenCV_Cpp
    ${SOURCES}
##    ${HEADERS}
)

# C++11
target_compile_features(OpenCV_Cpp
  PRIVATE cxx_std_11
)

# For nlohmann_json
find_package(nlohmann_json REQUIRED)

# For OpenCV
find_package(OpenCV REQUIRED)

message(STATUS "OpenCV library status:")
message(STATUS "version: ${nlohmann_json_VERSION}")
message(STATUS "libraries: ${nlohmann_json_LIBS}")
message(STATUS "include path: ${nlohmann_json_INCLUDE_DIRS}")

if(OpenCV_FOUND)
    target_include_directories(OpenCV_Cpp PRIVATE ${OpenCV_INCLUDE_DIRS})
    target_link_libraries(OpenCV_Cpp ${OpenCV_LIBS})
endif()