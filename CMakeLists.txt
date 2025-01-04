# cmake_minimum_required(VERSION 3.4...3.18)
# project(bayeselo LANGUAGES CXX)

# # 设置 C++ 标准和其他编译选项
# set(CMAKE_CXX_STANDARD 11)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -Wall")

# set(SRCS
#     ./BayesElo/version.cpp
#     ./BayesElo/pgnlex.cpp
#     ./BayesElo/str.cpp
#     ./BayesElo/const.cpp
#     ./BayesElo/date.cpp
#     ./BayesElo/pgnstr.cpp
#     ./BayesElo/move.cpp
#     ./BayesElo/consolui.cpp
#     ./BayesElo/clktimer.cpp
#     ./BayesElo/CTimeIO.cpp
#     ./BayesElo/chtime.cpp
#     ./BayesElo/readstr.cpp
#     ./BayesElo/ReadLineToString.cpp
#     ./BayesElo/CVector.cpp
#     ./BayesElo/CMatrix.cpp
#     ./BayesElo/CMatrixIO.cpp
#     ./BayesElo/CLUDecomposition.cpp
#     ./BayesElo/CBradleyTerry.cpp
#     ./BayesElo/CCDistribution.cpp
#     ./BayesElo/CCDistributionCUI.cpp
#     ./BayesElo/CCondensedResults.cpp
#     ./BayesElo/CDistribution.cpp
#     ./BayesElo/CDistributionCollection.cpp
#     ./BayesElo/CEloRatingCUI.cpp
#     ./BayesElo/CJointBayesian.cpp
#     ./BayesElo/CResultSet.cpp
#     ./BayesElo/CResultSetCUI.cpp
#     ./BayesElo/EloDataFromFile.cpp
#     ./BayesElo/CPredictionCUI.cpp
# )

# file(GLOB ALL_SRCS "./BayesElo/*.cpp")

# # add_executable(bayeselo ${SRCS})

# add_subdirectory(pybind11)
# # # pybind11_add_module(example example.cpp)
# pybind11_add_module(bayeselo py_bayeselo.cpp ${SRCS})

# add_executable(bayeselo_exe ${ALL_SRCS})

cmake_minimum_required(VERSION 3.14)
project(BayesElo)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置默认构建类型为 Release，如果用户未指定
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# 设置编译选项（针对 Release）
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /O2 /DNDEBUG")

# 查找 Python 和 pybind11
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
# find_package(pybind11 REQUIRED)
find_package(pybind11 REQUIRED HINTS "${Python3_SITELIB}")
# add_subdirectory(pybind11)

# 定义源文件列表（忽略部分 .cpp 文件）
set(SRCS
    ./BayesElo/version.cpp
    ./BayesElo/pgnlex.cpp
    ./BayesElo/str.cpp
    ./BayesElo/const.cpp
    ./BayesElo/date.cpp
    ./BayesElo/pgnstr.cpp
    ./BayesElo/move.cpp
    ./BayesElo/consolui.cpp
    ./BayesElo/clktimer.cpp
    ./BayesElo/CTimeIO.cpp
    ./BayesElo/chtime.cpp
    ./BayesElo/readstr.cpp
    ./BayesElo/ReadLineToString.cpp
    ./BayesElo/CVector.cpp
    ./BayesElo/CMatrix.cpp
    ./BayesElo/CMatrixIO.cpp
    ./BayesElo/CLUDecomposition.cpp
    ./BayesElo/CBradleyTerry.cpp
    ./BayesElo/CCDistribution.cpp
    ./BayesElo/CCDistributionCUI.cpp
    ./BayesElo/CCondensedResults.cpp
    ./BayesElo/CDistribution.cpp
    ./BayesElo/CDistributionCollection.cpp
    ./BayesElo/CEloRatingCUI.cpp
    ./BayesElo/CJointBayesian.cpp
    ./BayesElo/CResultSet.cpp
    ./BayesElo/CResultSetCUI.cpp
    ./BayesElo/EloDataFromFile.cpp
    ./BayesElo/CPredictionCUI.cpp
)

# 定义静态库
add_library(bayeselo_static STATIC ${SRCS})
set_target_properties(bayeselo_static PROPERTIES OUTPUT_NAME "bayeselo")

# 定义动态库
add_library(bayeselo_shared SHARED ${SRCS})
set_target_properties(bayeselo_shared PROPERTIES OUTPUT_NAME "bayeselo")

# 定义主程序 bayeselo
add_executable(bayeselo ./BayesElo/elomain.cpp ${SRCS})
target_link_libraries(bayeselo bayeselo_static)

# 定义 C++ 测试程序 test-cc
add_executable(test-cc test.cc)
target_link_libraries(test-cc bayeselo_shared)

# 定义 Python 扩展模块
pybind11_add_module(py_bayeselo MODULE ./py-bayeselo.cc ${SRCS})
# target_link_libraries(py_bayeselo PRIVATE bayeselo_shared Python3::Python)
set_target_properties(py_bayeselo PROPERTIES OUTPUT_NAME "bayeselo")

# 设置安装规则
install(TARGETS py_bayeselo
    LIBRARY DESTINATION ${Python3_SITEARCH}
)

# 添加测试
add_custom_target(test
    COMMAND ./test-cc
    COMMAND ${Python3_EXECUTABLE} ./test.py
    DEPENDS test-cc py_bayeselo
    COMMENT "Running tests..."
)