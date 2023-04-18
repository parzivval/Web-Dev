import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "../models";
import {CompanyService} from "../company.service";
import {ActivatedRoute} from "@angular/router";
import {VacancyService} from "../vacancy.service";

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {

  companies: Company[] = [];


  constructor(private companyService: CompanyService,  private vacancyService: VacancyService,private route: ActivatedRoute) {}

  ngOnInit() : void {
    this.getCompanies();
  }

  getCompanies() {
    this.companyService.getCompanies().subscribe((companies) => {
      this.companies = companies;
    });
    return this.companies;
  }





}
