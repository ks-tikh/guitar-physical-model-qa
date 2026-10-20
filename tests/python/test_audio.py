import os
import subprocess
import pytest

EXE_PATH = "./build/Debug/guitar_synth.exe"

def test_program_excution(build_and_run):
    assert os.path.exists("guitar_sound.wav")

def test_wav_file_exists(build_and_run):
    assert os.path.exists("guitar_sound.wav"), "Файл guitar_sound.wav не был создан!"

def test_wav_file_not_empty(build_and_run):
    assert os.path.getsize("guitar_sound.wav") > 44

def test_bug_freq_zero_should_fail():
    result = subprocess.run([EXE_PATH, "0"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "frequency" in result.stderr.lower()

def test_bug_freq_negative_should_fail():
    result = subprocess.run([EXE_PATH, "-100"], capture_output=True, text=True)
    assert result.returncode != 0

def test_bug_freq_high_should_fail():
    result = subprocess.run([EXE_PATH, "25000"], capture_output=True, text=True)
    assert result.returncode != 0