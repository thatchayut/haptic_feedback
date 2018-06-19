IDIR=/usr/local/include
LDIR=/usr/local/lib
CC=g++
CFLAGS=-O3 -Wall -I$(IDIR) -Winline -pipe -L$(LDIR)
LIBS=-lwiringPi -lwiringPiDev -lpthread -lm -lcrypt -lrt

OBJ=haptic_feedback.o

%.o: %.cpp
	$(CC) -c -o $@ $< $(CFLAGS)

haptic_feedback: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)
