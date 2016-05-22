#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-21 11:09:22
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : 1.7
from abc import ABCMeta, abstractmethod


class Price(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_price_code():
        pass

    @abstractmethod
    def get_charge(days_rented):
        pass

    def get_frequent_renter_points(days_rented):
        return 1


class ChildrensPrice(Price):
    """docstring for ChildrensPrice"""

    def get_price_code():
        return Movie.CHILDRENS

    def get_charge(days_rented):
        result = 1.5
        if days_rented > 3:
            result += (days_rented - 3) * 1.5
        return result


class RegularPrice(Price):
    """docstring for RegularPrice"""

    def get_price_code():
        return Movie.REGULAR

    def get_charge(days_rented):
        result = 2
        if days_rented > 2:
            result += (days_rented - 2) * 1.5
        return result


class NewReleasePrice(Price):
    """docstring for NewReleasePrice"""

    def get_price_code():
        return Movie.NEW_RELEASE

    def get_charge(days_rented):
        return days_rented * 3.0

    def get_frequent_renter_points(days_rented):
        return 2 if (days_rented > 1) else 1


class Movie(object):

    """docstring for Movie"""
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self.set_price_code(price_code)

    def get_price_code(self):
        return self._price.get_price_code()

    def set_price_code(self, price_code):
        price_dict = {
            self.CHILDRENS: ChildrensPrice,
            self.REGULAR: RegularPrice,
            self.NEW_RELEASE: NewReleasePrice
        }
        try:
            self._price = price_dict[price_code]
        except KeyError:
            raise ValueError('Incorrect Price Code')

    def get_title(self):
        return self._title

    def get_charge(self, days_rented):
        return self._price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented):
        return self._price.get_frequent_renter_points(days_rented)


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
        return self._movie.get_charge(self._days_rented)

    def get_frequent_renter_points(self):
        return self._movie.get_frequent_renter_points(self._days_rented)


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
    # c = Customer('moling')
    # c.add_rental(Rental(Movie('Zootopia', 2), 7))
    # c.add_rental(Rental(Movie('The Finest Hours', 0), 3))
    # c.add_rental(Rental(Movie('Angry Birds', 1), 2))
    # print(c.statament())
    # print(reduce(lambda x, y: x + y, [[1, 2], [3, 4], [], [5]], []))
