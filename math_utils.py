#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
import os, sys, argparse, math

class MathUtils():

    def is_odd(self, number):
        v = True 
        if number % 2==0: 
            v = False 
        return v
    
    def isprime(self, number):
        numnber = abs(int(number))
        if number < 2 : return False
        if number == 2 : return True
        if not number & 1 : return False
        for x in range (3 , int(number**0.5)+1, 2):
            if number % x == 0: 
                return False
        return True

    def next_prime(self, number):
         number = number +1
         while number:
            if self.isprime(number):
                return number
                break
            number = number+1

    def ith_prime(self, number):
        x = 2 
        count = 1
        while count < number :
            if self.isprime(x):
                x = self.next_prime(x)
                print "count:", count ,"prime:", x
                count +=1
        return x

    def sum_of_primes(self, number):
        skip = 1
        sum_ = 0 
        for x in xrange( 2, number+1, skip):
            if self.isprime(x):
                skip = self.next_prime(x)
                sum_ += x
        return sum_

    def prime_factor(self, number):
        if number <1: sys.exit(1)
        if number >=1:
            prime_factor = []
            skip =1
            for i in xrange(2, int(number**0.5)+1 ,skip):
                if self.isprime(i):
                    print "prime:", i,"factor", prime_factor
                    skip = i
                    if number % i == 0:
                        print "factor:", i                        
                        prime_factor.append(i)
                    if len(prime_factor) > 10:
                        prime_factor.popleft()
                        print set(prime_factor)

        return set(prime_factor)

    def is_palindrome(self, product):
        print product
        if len(product) < 2: return True
        if product[0] != product[-1]: return False
        
        return is_palindrome(product[-1:1])

    def sumsq_difference_sqsum(self, number):
        sumi =0
        sqsum =0
        for i in range(1, number+1):
            sumi += i
            sqsum += i**2
            print i, sumi , sqsum, sumi**2, sumi**2 - sqsum 
        return (sumi**2 - sqsum)

    def run(self, util, number):
        if util == 'next_prime':
            print  self.next_prime(number)
        elif util == 'prime_factor':
            print  self.prime_factor(number)
        elif util == 'is_odd':
            print self.is_odd(number)
        elif util == 'isprime':
            print self.isprime(number)
        elif util == 'largest_palindrome':
            print  self.largest_palindrome(number)
        elif util == 'sumsq_sqsum':
            print self.sumsq_difference_sqsum(number)
        elif util == 'ith_prime':
            print self.ith_prime(number)
        elif util == 'sum_of_primes':
            print self.sum_of_primes(number)
        else:
            print ' i dont understand'
            sys.exit(1) 
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("util")
    parser.add_argument("number")
    args = parser.parse_args()

    m = MathUtils()

    m.run(args.util, int(args.number) )

