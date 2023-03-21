package com.entity;

public class Shop {

	int price,quantity,id;
	String title,author;
	public Shop() {
		
	}
	public Shop(int id,int price ,int quantity,String title,String author) {
		this.id = id;
		this.price = price;
		this.quantity = quantity;
		this.title = title;
		this.author = author;
		
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public int getQuantity() {
		return quantity;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	
}
