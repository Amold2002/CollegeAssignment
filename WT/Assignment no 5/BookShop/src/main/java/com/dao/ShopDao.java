package com.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import com.entity.Shop;


public class ShopDao {

	Connection conn;

	public ShopDao(Connection conn) {

		this.conn = conn;
	}

	public boolean storeData(Shop s) {
		boolean f = false;

		try {
			String sql = "insert into ebookshop(book_id,book_title,book_author,book_price,quantity) values(?,?,?,?,?);";
			PreparedStatement ps = conn.prepareStatement(sql);
			ps.setInt(1, s.getId());
			ps.setString(2,s.getTitle());
			ps.setString(3, s.getAuthor());
			ps.setInt(4,s.getPrice());
			ps.setInt(5, s.getQuantity());

			int i = ps.executeUpdate();
			if (i == 1) {
				f = true;
			}
		} catch (SQLException e) {

			e.printStackTrace();
		}

		return f;
	}

}
