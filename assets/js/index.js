import React from 'react';
import ReactDOM from 'react-dom';
import { createRoot } from 'react-dom/client';
import InmateSearchProxy from './InmateSearchProxy.jsx';
import OrderReopenLink from './OrderReopenLink.jsx';
import InmateAddEditForm from './InmateAddEditForm';
import OrderCompleteForm from './OrderCompleteForm';
import OrderDetail from "./OrderDetail";
import OrderSummary from "./OrderSummary";

// bootstrap the React app by attaching InmateSearchProxy instance to their placeholders in the html template
const inmate_search_proxy_containers = document.querySelectorAll('.inmateSearchProxyContainer');
Array.from(inmate_search_proxy_containers).forEach(el => {
  const inmate_pk = el.attributes["data-inmate-id"].value;
  const root = createRoot(el);
  root.render(<InmateSearchProxy inmatePk={inmate_pk}/>);
});

const alert_link_containers = document.querySelectorAll('.orderReopenLink');
Array.from(alert_link_containers).forEach((el) => {
  const order_href = el.attributes["data-order-href"].value;
  const root = createRoot(el);
  root.render(<OrderReopenLink orderHref={order_href}/>);
});

const inmate_add_edit_form = document.querySelectorAll('.inmateAddEditForm');
Array.from(inmate_add_edit_form).forEach((el) => {
  const root = createRoot(el);
  root.render(<InmateAddEditForm/>);
});

const order_sendout = document.querySelectorAll('.orderCompleteForm');
Array.from(order_sendout).forEach((el) => {
  const root = createRoot(el);
  root.render(<OrderCompleteForm/>);
});

const order_detail = document.querySelectorAll('.orderDetail');
Array.from(order_detail).forEach((el) => {
  const root = createRoot(el);
  root.render(<OrderDetail/>);
});

const order_summary = document.querySelectorAll('.orderSummary');
Array.from(order_summary).forEach((el) => {
  const root = createRoot(el);
  root.render(<OrderSummary/>);
});
