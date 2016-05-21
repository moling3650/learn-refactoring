#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-21 11:09:22
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : 1.5


class Movie(object):

    """docstring for Movie"""
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, price_code):
        self._price_code = price_code

    def get_title(self):
        return self._title


class Rental(object):

    """Rental"""

    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie

    def get_charge(self):
        result = 0.0
        if self._movie.get_price_code() == Movie.REGULAR:
            result += 2
            if self._days_rented > 2:
                result += (self._days_rented - 2) * 1.5
        elif self._movie.get_price_code() == Movie.NEW_RELEASE:
            result += self._days_rented * 3
        elif self._movie.get_price_code() == Movie.CHILDRENS:
            result += 1.5
            if self._days_rented > 3:
                result += (self._days_rented - 3) * 1.5
        return result

    def get_frequent_renter_points(self):
        if self._movie.get_price_code() == Movie.NEW_RELEASE and self._days_rented > 1:
            return 2
        else:
            return 1


class Customer(object):

    """docstring for Customer"""

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def get_name(self):
        return self._name

    def statament(self):
        result = 'Rental Record for ' + self._name + '\n'
        for each in self._rentals:
            # show figures for this rental
            result += '\t' + each.get_movie().get_title() + '\t' + str(each.get_charge()) + '\n'

        # add footer lines
        result += 'Amount owed is ' + str(self._get_total_charge()) + '\n'
        result += 'You earned ' + str(self._get_total_frequent_renter_points()) + ' frequent renter points'
        return result

    def _get_total_charge(self):
        return sum(each.get_charge() for each in self._rentals)

    def _get_total_frequent_renter_points(self):
        return sum(each.get_frequent_renter_points() for each in self._rentals)

if __name__ == '__main__':
    c = Customer('moling')
    c.add_rental(Rental(Movie('Zootopia', 2), 7))
    c.add_rental(Rental(Movie('The Finest Hours', 0), 3))
    c.add_rental(Rental(Movie('Angry Birds', 1), 2))
    print(c.statament())
