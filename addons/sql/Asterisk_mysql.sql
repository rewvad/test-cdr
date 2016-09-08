

-- IMPORT MYSQL CDR DATABASE
-- -------------------------

-- If you are willing to edit the CDR from the admin panel, you will need to alter the original cdr table used by Asterisk and add a Primary Key.

-- The Following SQL commands will help:


CREATE TABLE cdr_new (
    id integer NOT NULL AUTO_INCREMENT PRIMARY KEY,
    src varchar(80) NOT NULL,
    dst varchar(80) NOT NULL,
    calldate datetime NOT NULL,
    clid varchar(80) NOT NULL,
    dcontext varchar(80) NOT NULL,
    channel varchar(80) NOT NULL,
    dstchannel varchar(80) NOT NULL,
    lastapp varchar(80) NOT NULL,
    lastdata varchar(80) NOT NULL,
    duration integer unsigned NOT NULL,
    billsec integer unsigned NOT NULL,
    disposition integer unsigned NOT NULL,
    amaflags integer unsigned NOT NULL,
    accountcode integer unsigned NOT NULL,
    uniqueid varchar(32) NOT NULL,
    userfield varchar(80) NOT NULL
);


INSERT INTO cdr_new (src,dst,calldate,clid,dcontext,channel,dstchannel,lastapp,lastdata,duration,billsec,disposition,amaflags,accountcode,uniqueid,userfield) SELECT src,dst,calldate,clid,dcontext,channel,dstchannel,lastapp,lastdata,duration,billsec,disposition,amaflags,accountcode,uniqueid,userfield FROM cdr;

RENAME TABLE cdr TO cdr_backup;

RENAME TABLE cdr_new TO cdr;


