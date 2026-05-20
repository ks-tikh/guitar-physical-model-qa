import os
import subprocess
import pytest

EXE_PATH = "./build/Debug/guitar_synth.exe"

def test_program_excution():
    result = subprocess.run([EXE_PATH], capture_output = True, text = True)

    assert result.returncode == 0, f"Программа упала с ошибкой: {result.stderr}"

def test_wav_file_exists():
    subprocess.run([EXE_PATH])

    assert os.path.exists("guitar_sound.wav"), "Файл guitar_soun.wav не был создан!"

def test_wav_file_not_empty():
    file_size = os.path.getsize("guitar_sound.wav")

    assert file_size > 44, "WAV файл слишком маленький, вероятно, пустой!"