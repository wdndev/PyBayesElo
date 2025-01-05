# Bayes Elo

## 1.简介

源码链接：[Bayesian-Elo](https://github.com/yytdfc/Bayesian-Elo/tree/master)

参考文档：[Bayesian Elo Rating](https://www.remi-coulom.fr/Bayesian-Elo/)

Python Bayesian Elo： [Release win python bayes elo · wdndev/PyBayesElo](https://github.com/wdndev/PyBayesElo/releases/tag/win_python_bayes_elo)

说明：本仓库代码，是在原来的仓库中进一步构建封装，方面在windows系统中构建和使用

## 2.CMake构建

需要安装 pybind11，使用如下命令安装：

```shell
pip install pybind11
```

CMake 构建，本人使用VS2022构建，可做参考

```shell
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

构建完成后，会在`build/Release`目录中查看生成的可执行文件和库文件

- bayeselo.exe ：可执行文件
- bayeselo.dll ：动态库
- bayeselo.cp310-win_amd64.pyd ： python库

注意：此方法构建的 bayeselo python库只支持特定版本的python；如果需要其他版本，切换不同python版本进行构建即可。

## 3.setuptools构建

需要安装`cibuildwheel`工具进行构建

- 安装 cibuildwheel：cibuildwheel 是一个工具，可以自动为不同 Python 版本生成 .whl 文件。

```shell
pip install cibuildwheel
```

- 使用 cibuildwheel 构建 .whl 文件：
  
```shell
cibuildwheel --output-dir wheelhouse
```

这将生成支持多个 Python 版本的 .whl 文件。


