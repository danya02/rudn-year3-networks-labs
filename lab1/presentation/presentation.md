---
lang: ru-RU
title: Лабораторная работа 1
author: |
  Генералов Даниил, НПИбд-01-21, 1032202280
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: 2023

toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Задача

> 1.3.1. Построение графиков в Octave
> 1.3.2. Разложение импульсного сигнала в частичный ряд Фурье
> 1.3.3. Определение спектра и параметров сигнала
> 1.3.4. Амплитудная модуляция
> 1.3.5. Кодирование сигнала. Исследование свойства самосинхронизации сигнала


# Выполнение 

## Octave

![Octave](../report/1.png)

## Отображение графика

![Plot](../report/2.png)

## Несколько графиков на одном рисунке

![Plot](../report/3.png)

## Меандр / квадратная волна

![Plot](../report/4.png)

## Квадратная волна через синусы
![Plot](../report/5.png)

## Преобразование Фурье
![Plot](../report/6.png)


## Исправленное преобразование Фурье
![Plot](../report/7.png)

## FFT(a+b) = FFT(a) + FFT(b)
![Plot](../report/8.png)

## Амплитудная модуляция
![Plot](../report/9.png)


## Кодирование разными методами

![Plot](../report/10.png)




# Вывод

Я получил опыт работы с Octave для расчета и визуализации данных на примере сигналов и их модуляции.

Разные коды имеют разную способность самосинхронизироваться.

## Manchester

![Plot](../work/coding/sync/manchester.png)

## Differenciated Manchester

![Plot](../work/coding/sync/diffmanc.png)

## Bipolar RZ

![Plot](../work/coding/sync/bipolarrz.png)

## AMI

![Plot](../work/coding/sync/ami.png)

## Unipolar

![Plot](../work/coding/sync/unipolar.png)

## Bipolar NRZ

![Plot](../work/coding/sync/bipolarnrz.png)
