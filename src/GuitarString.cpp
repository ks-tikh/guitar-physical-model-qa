#include "GuitarString.hpp"
#include <cmath>
#include <cstdlib>
#include <ctime> 

GuitarString::GuitarString(double frequency) {
    int N = static_cast<int>(std::round(sampling_rate / frequency));
    if (N < 2) N = 2;
    for (int i = 0; i < N; i++) {
        buffer.push_back(0.0);
    }
}

void GuitarString::pluck() {
    int size = buffer.size();
    buffer.clear();
    for (int i = 0; i < size; i++){
        double random_value = (rand() / (double)RAND_MAX) - 0.5;
        buffer.push_back(random_value);
    }
}

void GuitarString::tic(){
    if (buffer.size() < 2) return;

    double first = buffer[0];
    double second = buffer[1];
    double new_value = (first + second) * 0.5 * 0.994;

    buffer.push_back(new_value);
    buffer.pop_front();
}

double GuitarString::sample() const {
    if (buffer.empty()) return 0.0;
    return buffer.front();
}