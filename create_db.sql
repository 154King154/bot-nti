create table lama_logs
(
    chat_id   bigint            not null,
    date text,
    time text,
    type text,
    context text
);

alter table lama_logs
    owner to postgres;

create table lama_users
(
    chat_id   bigint            not null
);

alter table lama_users
    owner to postgres;

create table users
(
    chat_id   bigint            not null,
    date text,
    time text,
    username text,
    nickname text,
    department text,
    company text
);

alter table users
    owner to postgres;