package com.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.connection.Connect;
import com.dao.ShopDao;
import com.entity.Shop;

@WebServlet("/save")
public class RegisterServlet extends HttpServlet {

	
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int id =Integer.parseInt(req.getParameter("id")) ;
		String title = req.getParameter("title");
		String author = req.getParameter("author");
		int price =Integer.parseInt(req.getParameter("price")) ;
		int quantity =Integer.parseInt(req.getParameter("quantity")) ;
		
		
		Shop s = new Shop(id,price,quantity,title,author);
		
		ShopDao dao = new ShopDao(Connect.getConn());
		 boolean f=dao.storeData(s);
		if(f) {
			System.out.println("sucessfully data inserted");
		}else {
			System.out.println("Failed to insert the data");
		}
	}
	

}
