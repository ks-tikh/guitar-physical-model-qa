import os
import subprocess
import numpy as np
import pytest
from scipy.io import wavfile

EXE_PATH = "./build/Debug/guitar_synth.exe"


def estimate_fundamental_freq(signal: np.ndarray, sample_rate: int) -> float:
    x = signal.astype(np.float64)
    x = x - np.mean(x)  
    n = len(x)

    spectrum = np.fft.rfft(x, n=2 * n)
    acf = np.fft.irfft(np.abs(spectrum) ** 2)[:n]

    min_lag = sample_rate // 2000
    max_lag = sample_rate // 50
    region = acf[min_lag:max_lag]

    peaks = np.where((region[1:-1] > region[:-2]) & (region[1:-1] > region[2:]))[0] + 1
    first_strong_peak = peaks[region[peaks] > 0.85 * np.max(region)][0]
    period_samples = min_lag + first_strong_peak
    return sample_rate / period_samples


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


@pytest.mark.parametrize("target_freq", [110, 220, 440, 880])
def test_generated_frequency_matches_target(target_freq):
    result = subprocess.run([EXE_PATH, str(target_freq)], capture_output=True, text=True)
    assert result.returncode == 0

    sample_rate, data = wavfile.read("guitar_sound.wav")
    assert sample_rate == 44100

    detected_freq = estimate_fundamental_freq(data, sample_rate)
    assert detected_freq == pytest.approx(target_freq, rel=0.035)
