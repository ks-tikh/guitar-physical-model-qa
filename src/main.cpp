#include "GuitarString.hpp"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stdexcept>

void writeWavHeader(std::ofstream& file, int samplesCount) {
    int sampleRate = 44100;
    int numChannels = 1;
    int bitsPerSample = 16;

    file << "RIFF";
    int fileSize = 36 + samplesCount * 2;
    file.write(reinterpret_cast<char*>(&fileSize), 4);
    file << "WAVEfmt ";
    int fmtSize = 16;
    file.write(reinterpret_cast<char*>(&fmtSize), 4);
    short fmtType = 1; // PCM
    file.write(reinterpret_cast<char*>(&fmtType), 2);
    short channels = numChannels;
    file.write(reinterpret_cast<char*>(&channels), 2);
    file.write(reinterpret_cast<char*>(&sampleRate), 4);
    int byteRate = sampleRate * numChannels * bitsPerSample / 8;
    file.write(reinterpret_cast<char*>(&byteRate), 4);
    short blockAlign = numChannels * bitsPerSample / 8;
    file.write(reinterpret_cast<char*>(&blockAlign), 2);
    short bps = bitsPerSample;
    file.write(reinterpret_cast<char*>(&bps), 2);
    file << "data";
    int dataSize = samplesCount * 2;
    file.write(reinterpret_cast<char*>(&dataSize), 4);
}

int main(int argc, char* argv[]) {
    double freq = 440.0;
    double duration = 2.0; 
    if (argc > 1) {
        try {
            freq = std::stod(std::string(argv[1]));
        } catch (...) {
            std::cerr << "Invalid frequency argument\n";
            return 1;
        }
    }
        int sampleRate = 44100;
    int totalSamples = static_cast<int>(sampleRate * duration);

    try {
        GuitarString stringA(freq);
        stringA.pluck();

        std::ofstream wavFile("guitar_sound.wav", std::ios::binary);
        writeWavHeader(wavFile, totalSamples);

        for (int i = 0; i < totalSamples; ++i) {
            double s = stringA.sample();
            short intSample = static_cast<short>(s * 32767);
            wavFile.write(reinterpret_cast<char*>(&intSample), 2);
            stringA.tic();
        }
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    std::cout << "Success! File 'guitar_sound.wav' created." << std::endl;
    return 0;
}