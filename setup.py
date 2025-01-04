import sys
sys.path.append("D:/Software/miniconda3/envs/llm/Lib/site-packages")
from glob import glob
from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

src_files = [
    "./BayesElo/version.cpp",
    "./BayesElo/pgnlex.cpp",
    "./BayesElo/str.cpp",
    "./BayesElo/const.cpp",
    "./BayesElo/date.cpp",
    "./BayesElo/pgnstr.cpp",
    "./BayesElo/move.cpp",
    "./BayesElo/consolui.cpp",
    "./BayesElo/clktimer.cpp",
    "./BayesElo/CTimeIO.cpp",
    "./BayesElo/chtime.cpp",
    "./BayesElo/readstr.cpp",
    "./BayesElo/ReadLineToString.cpp",
    "./BayesElo/CVector.cpp",
    "./BayesElo/CMatrix.cpp",
    "./BayesElo/CMatrixIO.cpp",
    "./BayesElo/CLUDecomposition.cpp",
    "./BayesElo/CBradleyTerry.cpp",
    "./BayesElo/CCDistribution.cpp",
    "./BayesElo/CCDistributionCUI.cpp",
    "./BayesElo/CCondensedResults.cpp",
    "./BayesElo/CDistribution.cpp",
    "./BayesElo/CDistributionCollection.cpp",
    "./BayesElo/CEloRatingCUI.cpp",
    "./BayesElo/CJointBayesian.cpp",
    "./BayesElo/CResultSet.cpp",
    "./BayesElo/CResultSetCUI.cpp",
    "./BayesElo/EloDataFromFile.cpp",
    "./BayesElo/CPredictionCUI.cpp"
]

ext_modules=[
    Pybind11Extension(
        "bayeselo",
        src_files + ["py-bayeselo.cc",],  # Python 扩展模块的源文件
    )
]

setup(
    name="bayeselo",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_sage=False,
    python_requires=">=3.8",
)