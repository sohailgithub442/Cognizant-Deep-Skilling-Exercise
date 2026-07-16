import { Component } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter, RouterOutlet, RouterLink, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule],
  template: `
    <h2>Home Page</h2>

    <!-- Interpolation -->
    <h3>Welcome {{name}}</h3>

    <!-- Property Binding -->
    <img [src]="image" width="120">

    <br><br>

    <!-- Two-way Binding -->
    <input [(ngModel)]="name" placeholder="Enter Name">

    <p>You entered: {{name}}</p>

    <!-- Event Binding -->
    <button (click)="increase()">Click Me</button>

    <p>Button Clicked: {{count}} times</p>
  `
})
class HomeComponent {
  name = 'Angular';
  count = 0;
  image = 'https://angular.io/assets/images/logos/angular/angular.png';

  increase() {
    this.count++;
  }
}

@Component({
  selector: 'app-about',
  standalone: true,
  template: `
    <h2>About Page</h2>
    <p>This project demonstrates Angular CLI, Data Binding and Routing.</p>
  `
})
class AboutComponent {}

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent }
];

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `
    <h1>Angular CLI + Data Binding + Routing</h1>

    <a routerLink="/">Home</a> |
    <a routerLink="/about">About</a>

    <hr>

    <router-outlet></router-outlet>
  `
})
class AppComponent {}

bootstrapApplication(AppComponent, {
  providers: [provideRouter(routes)]
});
