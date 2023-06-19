<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kode = "";
    public $judul = "";
    public $penulis = "";
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
        $query = "INSERT INTO $this->table (`kode`,`judul`,`penulis`) VALUES ('$this->kode','$this->judul','$this->penulis')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode = '$this->kode', judul = '$this->judul', penulis = '$this->penulis' 
        WHERE id_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode($kode): int
    {
        $query = "UPDATE $this->table SET kode = '$this->kode', judul = '$this->judul', penulis = '$this->penulis' 
        WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_buku = $id";
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