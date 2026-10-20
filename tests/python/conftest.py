import subprocess
import pytest

EXE_PATH = "./build/Debug/guitar_synth.exe"

@pytest.fixture(scope="module", autouse=True)
def build_and_run():
    subprocess.run(["cmake", "--build", "build"], check=True)
    result = subprocess.run([EXE_PATH, "440"], capture_output=True, text=True)
    assert result.returncode == 0
    yield