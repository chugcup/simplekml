"""
Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt

Simplekml is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License

"""

class Coordinates(object):
    """Represents a list of Coordinate classes."""
    def __init__(self, coords=None):
        self._coords = []
        if coords is not None:
            self.addcoordinates(coords)

    def addcoordinates(self, coords):
        newcoords = []
        for coord in coords:
            # Cast to float; optionally includes altitude
            newcoords.append(
                tuple([float(n) for n in coord[:3]])
            )
        self._coords += newcoords

    def __str__(self):
        buf = []
        if not len(self._coords):
            return "0.0,0.0"
        for cd in self._coords:
            # Returns 2 (LNG,LAT) or 3 (LNG,LAT,ALT) coordinates
            buf.append(",".join([str(n) for n in cd[:3]]))
        return " ".join(buf)
