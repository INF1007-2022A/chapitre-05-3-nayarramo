#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from curses.ascii import isalnum
import math

def get_num_letters(text):
	num_letter=0
	for letter in text:
		num_letter += letter.isalnum()
	return num_letter

def get_word_length_histogram(text):
	list_words, len_words, histogram = text.split(" "), [], [0]
	for word in list_words:
		len_words += [get_num_letters(word)]
	len_words = [value for value in len_words if value != 0]
	for _ in range(max(len_words)):
		histogram.append(0)
	for length in len_words:
		histogram[length] += 1
	return histogram

def format_histogram(histogram):
	ROW_CHAR, position, form_hist = "*", 0, ""
	for i in range(1, len(histogram)):
		position+=1
		number = ROW_CHAR * histogram[i]
		form_hist += "\n" + f"{position:2} {number}"
	return form_hist

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	result = ""
	for i in range(1, max(histogram[1:])+1):
		for value in histogram[1:]:
			if value >= max(histogram[1:])+1-i:
				result+= BLOCK_CHAR
			else:
				result+= " "
		result+= "\n"
	result+= LINE_CHAR*len(histogram)
	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
