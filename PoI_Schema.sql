create table project (
    name        text primary key,
    description text,
    deadline    date
);

-- Tasks are steps that can be taken to complete a project
create table point_of_interest (
    id              integer primary key autoincrement not null,
    alt             float,
    climb           float,
    hspeed          float,
    lat             float,
    lon             float,
    mode            int,
    sats            int,
    sats_valid      int,
    time_btn_pushed text,
    track           float
);