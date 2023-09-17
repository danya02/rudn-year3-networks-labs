---
lang: ru-RU
title: Лабораторная работа 3
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

> 3.3.1.1.1. Изучение возможностей команды ipconfig для ОС типа Windows (ifconfig для систем типа Linux).
> 3.3.1.1.2. Определение MAC-адреса устройства и его типа.
> 3.3.2.1.1. Установить на домашнем устройстве Wireshark.
> 3.3.2.1.2. С помощью Wireshark захватить и проанализировать пакеты ARP и ICMP в части кадров канального уровня.
> 3.3.3.1. С помощью Wireshark захватить и проанализировать пакеты HTTP, DNS в части заголовков и информации протоколов TCP, UDP, QUIC.
> 3.3.4.1. С помощью Wireshark проанализировать handshake протокола TCP.


# Выполнение 

## ip addr

![ip addr](../report/1.png)

## ip link, route, neighbor

![ip link+route+neighbor](../report/2.png)


## 4c:cc:6a = MSI
![MSI](../report/3.png)

## 9c:b6:d0 = Rivet Networks

![Rivet](../report/4.png)

## Wireshark

![wireshark](../report/5.png)

## ICMP Echo

![icmp echo](../report/6.png)

## ICMP Echo Reply

![icmp echo reply](../report/7.png)

## ARP

![arp](../report/8.png)

## Ping rudn.ru

![rudn.ru](../report/9.png)

## DNS-запрос

![dns query](../report/10.png)

## DNS-ответ

![dns response](../report/11.png)

## Ping

![ping](../report/12.png)

## HTTP

![http](../report/13.png)


## TLS Client Hello

![tls client hello](../report/14.png)

## TLS Server Hello

![tls server hello](../report/15.png)


## QUIC

![quic](../report/16.png)

## QUIC

![quic](../report/17.png)


## TCP

![tcp](../report/18.png)

## TCP SYN

![tcp syn](../report/19.png)

## TCP SYN ACK

![tcp syn ack](../report/20.png)

## TCP ACK

![tcp ack](../report/21.png)

## TCP PSH ACK

![tcp psh ack client](../report/22.png)

## TCP PSH ACK

![tcp psh ack server](../report/23.png)

## TCP FIN ACK

![tcp fin ack](../report/24.png)


## Вывод

Я получил опыт работы с Wireshark для анализа пакетов в сети, а также с общими правилами работы различных сетевых протоколов.
