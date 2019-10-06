-- Create table
create table USER_INFO
(
  name     VARCHAR2(30),
  age      NUMBER,
  birthday DATE
);
-- Add comments to the table
comment on table USER_INFO
  is '测试用户表';
-- Add comments to the columns
comment on column USER_INFO.name
  is '用户名';
comment on column USER_INFO.age
  is '年龄';
comment on column USER_INFO.birthday
  is '出生年月日';

-- 插入数据
insert into user_info(name,age,birthday)
values ('faith.huan',30,to_date('1988-10-26','yyyy-mm-dd'));
