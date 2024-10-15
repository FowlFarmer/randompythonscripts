

/**
 * @file variadicTemplateDemo.cpp
 * @author your name (you@domain.com)
 * @brief I came across this method in CPP to take as many args in a function as
 * needed and recursively call less overloaded functions. I thought it was very
 * cool.
 * 
 * atomicIncrement uses variadic template to lock a mutex and increment as many variables you need.
 * 
 * @version 0.1
 * @date 2024-10-15
 *
 * @copyright Copyright (c) 2024
 *
 */

template<typename T, typename... Args>
void increment(T& arg0, Args... args){
    ++arg0;
    increment(args...);
}

void increment(){}

template<typename... Args>
void atomicIncrement(std::mutex mutex, Args... args){
    std::lock_guard<std::mutex> lock(mutex);
    increment(args...);
}