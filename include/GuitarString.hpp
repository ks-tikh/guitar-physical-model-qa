#ifndef GUITAR_STRING_HPP
#define GUITAR_STRING_HPP

#include <vector>
#include <deque>

class GuitarString {
private:
    std::deque<double> buffer;
    int sampling_rate = 44100;

public:
    GuitarString(double frequency);
    void pluck();
    void tic();
    double sample() const;
};

#endif