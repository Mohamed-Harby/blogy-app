drop database blogy;
create database blogy;
use blogy;


create table user
(
    id       int auto_increment,
    username varchar(20) not null,
    email    varchar(20) not null,
    password varchar(30) not null,
    photo blob,
    primary key (id)
);

create table post
(
    id      int auto_increment,
    user_id int not null,
    title   varchar(50),
    content varchar(1000),
    primary key (id),
    foreign key (user_id) references user (id) on delete cascade
);

create table emotion
(
    user_id int,
    post_id int,
    type    varchar(10) check ( type in ('idea', 'like', 'dislike') ),
    primary key (user_id, post_id),
    foreign key (user_id) references user (id) on delete cascade,
    foreign key (post_id) references post (id) on delete cascade
);


create table friendship(
    first_friend_id int,
    second_friend_id int,
    primary key (first_friend_id, second_friend_id),
    foreign key (first_friend_id) references user(id),
    foreign key (second_friend_id) references user(id)
)
