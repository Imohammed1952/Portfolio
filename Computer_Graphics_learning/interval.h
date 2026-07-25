#ifndef INTERVAL_H
#define INTERVAL_H

#include "rtweekend.h" // For intellisense to recognize infinity constant

class interval{
    public:
        double min;
        double max;

        interval() {
            min = +infinity;
            max = -infinity;
        };

        interval(double min, double max){
            this->min = min;
            this->max = max;
        };

        bool contains(double x) const {
            return (min <= x && x <= max);
        };

        bool surrounds(double x) const {
            return (min < x && x < max);
        };

        static const interval empty, universe;
    };

const interval interval::empty = interval(+infinity, -infinity);
const interval interval::universe = interval(-infinity, +infinity);



#endif