cmake_minimum_required(VERSION 3.27)
project(OpenCV_Cpp)

# Copy resouce
#file(COPY ${CMAKE_SOURCE_DIR}/media/ DESTINATION ${PROJECT_BINARY_DIR}/media/)
#add_definitions(-DRESOURCE_DIR="${PROJECT_BINARY_DIR}/media/")

# Create Main project
set(SOURCES
    56_adaptiveThreshold.cpp
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

# For OpenCV
find_package(OpenCV REQUIRED)
if(OpenCV_FOUND)
    target_include_directories(OpenCV_Cpp PRIVATE ${OpenCV_INCLUDE_DIRS})
    target_link_libraries(OpenCV_Cpp ${OpenCV_LIBS})
endif()