<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $kode = "";
    public $tanggal_pinjam = "";
    public $tanggaal_kembali = "";
    public $id_buku = "";
    public $id_anggota = "";
    public $id_petugas = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode(int $kode)
    {
        $query = "SELECT * FROM $this->table WHERE kode = $kode";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode`,`tanggal_pinjam`,`tanggaal_kembali`,`id_buku`,`id_anggota`,`id_petugas`) VALUES ('$this->kode','$this->tanggal_pinjam','$this->tanggaal_kembali','$this->id_buku','$this->id_anggota','$this->id_petugas')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode = '$this->kode', tanggal_pinjam = '$this->tanggal_pinjam', tanggaal_kembali = '$this->tanggaal_kembali', id_buku = '$this->id_buku', id_anggota = '$this->id_anggota', id_petugas = '$this->id_petugas' 
        WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode($kode): int
    {
        $query = "UPDATE $this->table SET kode = '$this->kode', tanggal_pinjam = '$this->tanggal_pinjam', tanggaal_kembali = '$this->tanggaal_kembali', id_buku = '$this->id_buku', id_anggota = '$this->id_anggota', id_petugas = '$this->id_petugas' 
        WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode($kode): int
    {
        $query = "DELETE FROM $this->table WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>