# BUG-001: Нет валидации frequency <=0 и >= Nyquist

**Summary:** При frequency=0 и 25000 не кидается ошибка, создается *.wav

**Steps:**
1. .\build\Debug\guitar_synth.exe 0

**Expected:** exit 1, Error: frequency must be > 0

**Actual (до фикса):** exit 0, создался guitar_sound.wav (N=2)

**Severity:** Medium | **Priority:** High

**Status:** Fixed (commit fix/N-rounding)

**Environment:** Windows, sampleRate 44100, commit до фикса