<?php
//Simpanlah dengan nama file : Petugas.php
require_once 'database.php';
class Petugas 
{
    private $db;
    private $table = 'petugas';
    public $kode = "";
    public $nama = "";
    public $telepon = "";
    public $alamat = "";
    public $jk = "";
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
        $query = "INSERT INTO $this->table (`kode`,`nama`,`telepon`,`alamat`,`jk`) VALUES ('$this->kode','$this->nama','$this->telepon','$this->alamat','$this->jk')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode = '$this->kode', nama = '$this->nama', telepon = '$this->telepon', alamat = '$this->alamat', jk = '$this->jk' 
        WHERE id_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode($kode): int
    {
        $query = "UPDATE $this->table SET kode = '$this->kode', nama = '$this->nama', telepon = '$this->telepon', alamat = '$this->alamat', jk = '$this->jk' 
        WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_petugas = $id";
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