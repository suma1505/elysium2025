<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%
    String name = (String) session.getAttribute("name");
    if (name == null) {
        response.sendRedirect("/login");
        return;
    }
%>

<h1>Welcome <%= name %></h1>
<a href="/logout">Logout</a>