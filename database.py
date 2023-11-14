from tkinter import *
from tkinter import messagebox
root = Tk()
import sqlite3
con=sqlite3.Connection("bus_reservation_211b349")
cur=con.cursor()
cur.execute('create table route_details(RID varchar(6),station_name varchar(20), SID int(3), constraint route_pk primary key (RID,SID))')
cur.execute('create table operator_details(operator_name varchar(40),OID varchar(6) primary key,address varchar(50), phone_number bigint(12), Email varchar(30))')
cur.execute('create table bus_details(BID varchar(6) primary key,Bus_Type varchar(20),Op_name varchar(35), operator_id varchar(6), route_id varchar(5),seat_capacity smallint(2), fare int(6), constraint fk_oid foreign key (operator_id) references operator(OID), constraint fk_rid foreign key (route_id) references route_details(RID))')
cur.execute('create table running_details(RBID varchar(6), running_date date, seat_available smallint(2), constraint run_pk primary key(running_date,RBID),foreign key (RBID) references bus_details(BID))')
cur.execute('create table booking_history(pname varchar(20), gender char(5), age smallint(3),mobile bigint(10) primary key,bus varchar(6) ,travelling_date date,booking_date date,no_of_seats smallint(2),total_fare int(6), booking_ref_number int(5),foreign key (bus) references bus_details(BID))')


cur.execute('''insert into route_details values('MPRT1','Guna',1),('MPRT1','Biaora',2),('MPRT1','Bhopal',3),('MPRT2','Guna',3),('MPRT2','Biaora',2),('MPRT2','Bhopal',1),('MPRT3','Guna',1),('MPRT3','Dewas',2),('MPRT3','Indore',3),('MPRT4','Guna',3),('MPRT4','Dewas',2),('MPRT4','Indore',1),('UPRT1','Guna',1),('UPRT1','Jhansi',2),('UPRT1','Kanpur',3),('UPRT1','Lucknow',4),('UPRT2','Lucknow',1),('UPRT2','Kanpur',2),('UPRT2','Jhansi',3),('UPRT2','Guna',4),('UPRT3','Guna',1),('UPRT3','Jhansi',2),('UPRT4','Guna',2),('UPRT4','Jhansi',1),('RJRT1','Guna',1),('RJRT1','Baran',2),('RJRT1','Kota',3),('RJRT2','Guna',3),('RJRT2','Baran',2),('RJRT2','Kota',1)''')
cur.execute('''insert into operator_details values('Daresi Travels','OPMP1','Daresi Travels, Guna',07542222176,'travelsdaresi@gmail.com'),('Raja Bus Service','OPGJ1','Raja travels, Surat, Gujarat',07314288888,'rajatravels@gmail.com'),('Hans Travels','OPMP2','Indore 15/3, Indore',07312510007,'hans.travels@yahoo.com '),('Kamla Travels','OPMP3','Kamla Travels 13,Indore,M.P.',07314090788,'shivys10@gmail.com'),('Amar Travels','OPMP4','Amar travels office rishivihar, Gwalior, M.P.',9425748083,'amartravels12@gmail.com'),('Bharti Tours And Travels','OPRJ1','H-79,Lal bagh,Dhyanchand Marg,Kota',9829056423,'info@bhartitours.com'),('Samay Shatabdi Travels','OPUP1','Shatabdi Terminal,Kanpur',7518904313,'help@samayshatabditravels.com')''')
cur.execute('''insert into bus_details values('MP1B1','AC 2x2','Daresi Travels','OPMP1','MPRT1',40,400),('GJ1B1','AC 2x2','Raja Bus Service','OPGJ1','MPRT1',40,320),('MP2B1','AC SLEEPER 2x1','Hans Travels','OPMP2','MPRT1',40,333),('GJ1B2',' NON AC 2x2','Raja Bus Service','OPGJ1','MPRT1',40,320),('MP1B3','AC 2x2','Daresi Travels','OPMP1','MPRT2',40,220),('GJ1B3','AC 2x2','Raja Bus Travels','OPGJ1','MPRT2',40,320),('MP3B1','NON AC SLEEPER 2x1','Kamla Travels','OPMP3','MPRT2',40,900),('GJ1B4','AC 2x2','Raja Bus Service','OPGJ1','MPRT3',40,487),('MP2B2','NON AC 2x1','Hans Travels','OPMP2','MPRT3',40,380),('GJ1B5','AC 2x2','Raja Bus Service','OPGJ1','MPRT4',40,490),('MP2B3','NON AC SLEEPER 2x1','Hans Travels','OPMP2','MPRT4',40,400),('RJ1B1','AC SLEEPER 2x1','Bharti Tour And Travels','OPRJ1','RJRT1',40,900),('UP1B1','AC SLEEPER 2x1','Samay Shatabdi Travels','OPUP1','UPRT1',40,1300),('MP4B1','AC SLEEPER 2x1','Amar Travels','OPMP4','UPRT2',40,1250),('MP3B2','NON AC SLEEPER 2x1','Kamla Travels','OPMP3','UPRT2',40,1000)''')
cur.execute('''insert into running_details values('MP1B1','2022-11-30',40),( 'MP1B1','2022-12-01',40),( 'MP1B1','2022-12-02',40),( 'MP1B1','2022-12-03',40),( 'MP1B1','2022-12-04',40),( 'MP1B1','2022-12-05',40),( 'MP1B2','2022-12-01',40),( 'MP1B2','2022-12-02',40),( 'MP1B2','2022-12-04',40),( 'MP1B2','2022-12-05',40),('GJ1B1','2022-11-30',40),('GJ1B1','2022-12-02',40),('GJ1B1','2022-12-04',40),('GJ1B1','2022-12-05',40),('MP2B1','2022-11-30',40),('MP2B1','2022-12-01',40),('MP2B1','2022-12-03',40),('MP2B1','2022-12-04',40),('GJ1B2','2022-11-30',40),('GJ1B2','2022-12-01',40),('GJ1B2','2022-12-02',40),('GJ1B2','2022-12-03',40),('GJ1B2','2022-12-05',40),('MP1B3','2022-12-01',40),('MP1B3','2022-12-02',40),('MP1B3','2022-12-03',40),('MP1B3','2022-12-4',40),('MP1B3','2022-12-05',40),('GJ1B3','2022-11-30',40),('GJ1B3','2022-12-02',40),('GJ1B3','2022-12-04',40),('GJ1B3','2022-12-05',40),('MP3B1','2022-12-01',30),('MP3B1','2022-12-02',40),('MP3B1','2022-12-03',40),('MP3B1','2022-12-4',40),('MP3B1','2022-12-05',40),('GJ1B4','2022-11-30',40),('GJ1B4','2022-12-01',40),('GJ1B4','2022-12-02',40),('GJ1B4','2022-12-03',40),('GJ1B4','2022-12-05',40),('MP2B3','2022-11-30',40),('MP2B3','2022-12-01',40),('MP2B3','2022-12-03',40),('MP2B3','2022-12-04',40),( 'RJ1B1','2022-11-30',40),( 'RJ1B1','2022-12-01',40),( 'RJ1B1','2022-12-02',40),( 'RJ1B1','2022-12-03',40),( 'RJ1B1','2022-12-04',40),( 'RJ1B1','2022-12-05',40),( 'UP1B1','2022-11-30',40),( 'UP1B1','2022-12-01',40),( 'UP1B1','2022-12-02',40),( 'UP1B1','2022-12-03',40),( 'UP1B1','2022-12-04',40),( 'UP1B1','2022-12-05',40),( 'MP4B1','2022-11-30',40),( 'MP4B1','2022-12-01',40),( 'MP4B1','2022-12-02',40),( 'MP4B1','2022-12-03',40),( 'MP4B1','2022-12-04',40),( 'MP4B1','2022-12-05',40),('MP3B2','2022-12-01',40),('MP3B2','2022-12-02',40),('MP3B2','2022-12-03',40),('MP3B2','2022-12-4',40),('MP3B2','2022-12-05',40)''')
cur.execute('create table user(username varchar(20) primary key,password varchar(20))')

con.commit()
con.close()
