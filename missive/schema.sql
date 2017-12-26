# DEPRECATED: this is for when the DB was being created with sqlite
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
