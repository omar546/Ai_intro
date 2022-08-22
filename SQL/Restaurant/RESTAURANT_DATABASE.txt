CREATE TABLE Restaurant (
 Res_Name VARCHAR(20) , 
 Manager_ID INT NOT NULL, 
 Branch_Num VARCHAR(20) , 
 Res_Address VARCHAR(40) , 
 Tel_Number INT , 
 PRIMARY KEY (Res_Name),
 UNIQUE (Manager_ID) 
);

CREATE TABLE Supplier( 
 Supplier_ID INT , 
 Sup_Name VARCHAR(20) , 
 Sup_Address VARCHAR(40) , 
 Supplies VARCHAR(20) ,
 PRIMARY KEY (Supplier_ID )
);

CREATE TYPE Employee AS OBJECT (
 Emp_ID INT,
 Emp_Name VARCHAR(20) ,
 Emp_Salary INT ,
 Emp_Tel_Num INT , 
 Res_Name VARCHAR(20)
 
)NOT FINAL;


CREATE TABLE Employee_T OF Employee;


ALTER TABLE Employee_T 
ADD CONSTRAINT em_pk PRIMARY KEY (Emp_ID);

ALTER TABLE Employee_T 
ADD CONSTRAINT em_fk FOREIGN KEY (Res_Name) REFERENCES Restaurant (Res_Name) ON DELETE CASCADE ;

CREATE TYPE Cashier UNDER Employee (
 Cashier_ID INT ,
 Reg_Num INT
);

CREATE TABLE Cashier_T OF Cashier;

ALTER TABLE Cashier_T 
ADD CONSTRAINT ca_pk PRIMARY KEY (Cashier_ID);

ALTER TABLE Cashier_T 
ADD CONSTRAINT ca_fk FOREIGN KEY (Res_Name) REFERENCES Restaurant (Res_Name) ON DELETE CASCADE ;

CREATE TYPE Chef UNDER Employee (
 Chef_ID INT ,
 Kitchen_Num INT
);

CREATE TABLE Chef_T OF Chef;

ALTER TABLE Chef_T 
ADD CONSTRAINT ch_pk PRIMARY KEY (Chef_ID);

ALTER TABLE Chef_T 
ADD CONSTRAINT ch_fk FOREIGN KEY (Res_Name) REFERENCES Restaurant (Res_Name) ON DELETE CASCADE ;

CREATE TYPE Waiter UNDER Employee (
 Waiter_ID INT,
 Tables_Num INT
);

CREATE TABLE Waiter_T OF Waiter;

ALTER TABLE Waiter_T
ADD CONSTRAINT wa_pk PRIMARY KEY (Waiter_ID);

ALTER TABLE Waiter_T
ADD CONSTRAINT wa_fk FOREIGN KEY (Res_Name) REFERENCES Restaurant (Res_Name) ON DELETE CASCADE ;

CREATE TABLE Waiters_Tables(
 Waiter_ID INT,
 Tables_Num INT,
 CONSTRAINT wt_fk FOREIGN KEY (Waiter_ID) REFERENCES Waiter_T (Waiter_ID) ON DELETE CASCADE
);

CREATE TABLE Customer(
 Contact_Num INT ,
 Cust_Name VARCHAR(20) ,
 Cust_Address VARCHAR(40) ,
 CONSTRAINT cu_pk PRIMARY KEY (Contact_Num)
);

CREATE TABLE Bill(
 Bill_Num INT ,
 Cashier_ID INT NOT NULL,
 Bill_Price FLOAT ,
 Order_Detail VARCHAR(100) ,
 Contact_Num INT ,
 CONSTRAINT bi_pk PRIMARY KEY (Bill_Num) ,
 CONSTRAINT bi_fk FOREIGN KEY (Contact_Num) REFERENCES Customer (Contact_Num) ON DELETE CASCADE,
 CONSTRAINT bi_fk2 FOREIGN KEY (Cashier_ID)REFERENCES Cashier_T (Cashier_ID)ON DELETE CASCADE
);

CREATE TABLE Order_(
 Order_Num INT ,
 Item_Counts INT NOT NULL ,
 Contact_Num INT ,
 Waiter_ID INT ,
 CONSTRAINT or_pk PRIMARY KEY (Order_Num)
);
ALTER TABLE Order_ 
ADD CONSTRAINT or_fk1 FOREIGN KEY (Contact_Num) REFERENCES Customer (Contact_Num) ON DELETE CASCADE ;

ALTER TABLE Order_ 
ADD CONSTRAINT or_fk2 FOREIGN KEY (Waiter_ID) REFERENCES Waiter_T (Waiter_ID) ON DELETE CASCADE ;

CREATE TABLE Item(
 Item_ID INT ,
 Item_Price FLOAT ,
 Quantity INT,
 Description VARCHAR(300),
 CONSTRAINT it_pk PRIMARY KEY (Item_ID)
);

CREATE TABLE Prepare(
 Chef_ID INT ,
 Order_Num INT ,
 PRIMARY KEY (Chef_ID,Order_Num) ,
 CONSTRAINT pr_fk1 FOREIGN KEY (Chef_ID) REFERENCES Chef_T (Chef_ID) ON DELETE CASCADE ,
 CONSTRAINT pr_fk2 FOREIGN KEY (Order_Num) REFERENCES Order_ (Order_Num) ON DELETE CASCADE
);

CREATE TABLE Serve(
 Contact_Num INT ,
 Waiter_ID INT ,
 PRIMARY KEY (Contact_Num,Waiter_ID) ,
 CONSTRAINT se_fk1 FOREIGN KEY (Contact_Num) REFERENCES Customer (Contact_Num) ON DELETE CASCADE ,
 CONSTRAINT se_fk2 FOREIGN KEY (Waiter_ID) REFERENCES Waiter_T (Waiter_ID) ON DELETE CASCADE
);

CREATE TABLE Contains(
 Item_ID INT ,
 Q_Item INT ,
 Order_Num INT ,
 PRIMARY KEY (Item_ID,Order_Num) ,
 CONSTRAINT co_fk1 FOREIGN KEY (Item_ID) REFERENCES Item (Item_ID) ON DELETE CASCADE ,
 CONSTRAINT co_fk2 FOREIGN KEY (Order_Num) REFERENCES Order_ (Order_Num) ON DELETE CASCADE
);
