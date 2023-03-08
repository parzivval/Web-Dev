import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Album, Photo} from "./models";
import {AlbumsComponent} from "./albums/albums.component";
@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  BASE_URL: string = "https://jsonplaceholder.typicode.com";
  constructor(private client: HttpClient) {
  }
  getAlbums() : Observable<Album[]>{
    return this.client.get<Album[]>(`${this.BASE_URL}/albums`);//get albums
  }
  getAlbum(id: number) : Observable<Album> {
    return this.client.get<Album>(`${this.BASE_URL}/albums/${id}`);//get album
  }
  addAlbum(album: Album) : Observable<Album> {
    return this.client.post<Album>(`${this.BASE_URL}/albums`, album);//new album
  }
  deleteAlbum(id: number) : Observable<Album> {
    return this.client.delete<Album>(`${this.BASE_URL}/albums/${id}`);//delete album
  }
  updateAlbum(album: Album, id: number) : Observable<Album> {
    return this.client.put<Album>(`${this.BASE_URL}/albums/${id}`, album);//update album
  }
  getAlbumPhotos(id: number)  : Observable<Photo[]> {
    return this.client.get<Photo[]>(`${this.BASE_URL}/albums/${id}/photos`);//get album photos
  }


}
