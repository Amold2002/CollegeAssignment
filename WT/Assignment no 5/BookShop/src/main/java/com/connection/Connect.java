package com.connection;

import java.sql.Connection;
import java.sql.DriverManager;

public class Connect {

	static Connection conn;

	public static Connection getConn() {

		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/college", "root", "9503359529");
		} catch (Exception ex) {
			System.out.println(ex);
		}
		return conn;
	}

}