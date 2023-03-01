import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product, products } from '../products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  products = products;
  @Input() selectedProduct: string | undefined;

  like(product: Product){
    product.likes += 1;
  }
  delete(product: Product){
    for(let i=0; i<products.length; i++){
      if(products[i] == product){
    delete products[i];
    break;
      }
    }
  }

  share(product: { link: string }) {
    window.open('https://telegram.me/share/url?url=' + product.link);
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }

}
